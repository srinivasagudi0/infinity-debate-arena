# main.py

from Opponent import Opponent
from difficulty import DIFFICULTY_MODES
from memory import DebateMemory
from persistent_memory import load_last_topic, save_last_topic
from timer import TurnTimer
import re

print("🔥 Welcome to Infinity Debate Arena 🔥\n")

# ---- TOPIC HANDLING (WITH RESUME) ----

last_topic = load_last_topic()

def validate_topic(raw_topic: str):
    """
    Lightweight local checks for ambiguous or too-short topics.
    Returns dict: {status: 'ok'|'ambiguous'|'reject', suggestions: [], reason: str}
    """
    t = (raw_topic or "").strip()
    if not t:
        return {"status": "reject", "suggestions": [], "reason": "Empty topic."}

    pronouns = {"he","she","they","it","him","her","them","his","hers","their","this","that","these","those"}
    words = re.findall(r"\w+", t.lower())
    if len(words) == 1 and words[0] in pronouns:
        return {
            "status": "ambiguous",
            "suggestions": [
                f"Clarify who '{words[0]}' refers to (e.g. \"{words[0]} (the CEO) vs {words[0]} (the athlete)\").",
                "Use a concrete topic such as 'Climate change policy' or 'Universal basic income'."
            ],
            "reason": "Single pronoun — unclear subject."
        }
    if len(t) < 3 or len(words) < 2:
        return {
            "status": "ambiguous",
            "suggestions": ["Make the topic more descriptive (include subject and scope), e.g. 'Should governments fund X?'"],
            "reason": "Topic too short or vague."
        }
    return {"status": "ok", "suggestions": [], "reason": ""}

# ---- TOPIC HANDLING (WITH RESUME AND LOCAL VALIDATION) ----

topic_input = input(
    "Enter a debate topic\n"
    "(or type 'resume', 'resume on <topic>', or 'exit'):\n> "
).strip()

if topic_input.lower() == "exit":
    print("Exiting the debate arena. Goodbye!")
    exit()

if topic_input.lower() == "resume":
    if last_topic:
        topic = last_topic
        print(f"\n🔁 Resuming last debate on: {topic}")
    else:
        print("❌ No previous debate found.")
        topic = input("Enter a new debate topic:\n> ").strip()

elif topic_input.lower().startswith("resume on "):
    topic = topic_input[10:].strip()
    print(f"\n🔁 Resuming debate on new topic: {topic}")

else:
    # new topic: local validation and simple suggestion loop (no OpenAI calls here)
    candidate = topic_input
    while True:
        verdict = validate_topic(candidate)
        status = verdict["status"]
        suggestions = verdict.get("suggestions", [])
        reason = verdict.get("reason", "")

        if status == "ok":
            topic = candidate
            break

        if status == "reject":
            print(f"\n❌ Topic rejected: {reason}\nPlease enter a different topic:")
            candidate = input("> ").strip()
            continue

        # ambiguous
        print("\n🔎 Topic check: unclear.")
        if reason:
            print("Reason:", reason)
        if suggestions:
            print("\nSuggestions:")
            for i, s in enumerate(suggestions, 1):
                print(f"{i}. {s}")
            print("0. Keep original topic")
            choice = input("Choose a suggestion number to accept, or type a new topic:\n> ").strip()
            if choice.isdigit():
                idx = int(choice)
                if idx == 0:
                    topic = candidate
                    break
                if 1 <= idx <= len(suggestions):
                    topic = suggestions[idx-1]
                    print(f"\n✅ Using suggested topic: {topic}")
                    break
            # treat input as new topic text
            candidate = choice or input("Enter new topic:\n> ").strip()
        else:
            candidate = input("Please clarify the topic (or enter a new one):\n> ").strip()

save_last_topic(topic)

print(f"\n📌 Debate Topic Locked: {topic}")

# ---- DIFFICULTY SELECTION (STRICT: 3 ONLY) ----

print("\nSelect Difficulty:")
print("1 - Beginner")
print("2 - Advanced")
print("3 - Expert")

difficulty = None
while difficulty not in DIFFICULTY_MODES:
    difficulty = input("Choose difficulty (1/2/3): ").strip()
    if difficulty not in DIFFICULTY_MODES:
        print("❌ Invalid choice. Select 1, 2, or 3 only.")

mode = DIFFICULTY_MODES[difficulty]

print(f"\n⚔️ Difficulty Locked: {mode['name']}")
print(f"⏱️ Time per turn: {mode['time_limit']} seconds")

# ---- SETUP MEMORY + OPPONENT ----

memory = DebateMemory(max_turns=6)

opponent = Opponent(
    name=f"DebateBot ({mode['name']})",
    strategy=mode["strategy"],
    memory=memory
)

print("\n🏟️ Debate Arena Ready!")
print("Type 'exit' anytime to leave.\n")

# ---- DEBATE LOOP WITH TIMER ----

while True:
    print(f"⏳ You have {mode['time_limit']} seconds.")
    timer = TurnTimer(mode["time_limit"])
    timer.start()

    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\n👋 Exiting the debate arena. Goodbye!")
        break

    prompt = f"Debate topic: {topic}\nUser argument: {user_input}"
    response = opponent.respond(prompt)

    print(f"\n{opponent.name}: {response}\n")
