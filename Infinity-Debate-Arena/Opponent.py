# opponent.py

import os
from openai import OpenAI

# Replace hardcoded key with environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY environment variable not set. "
        "Export it in your shell before running, e.g.:\n"
        "  export OPENAI_API_KEY='sk-...'\n"
    )

client = OpenAI(api_key=api_key)

class Opponent:
    def __init__(self, name: str, strategy: str, memory):
        self.name = name
        self.strategy = strategy
        self.memory = memory

    def respond(self, prompt: str) -> str:
        messages = [
            {
                "role": "system",
                "content": f"You are {self.name}. Strategy: {self.strategy}"
            }
        ]

        # Inject memory
        messages.extend(self.memory.get())

        # Current user input
        messages.append({"role": "user", "content": prompt})

        response = client.responses.create(
            model="gpt-4.1-mini",#feel free to change the model
            input=messages
        )

        reply = response.output_text

        # Store memory
        self.memory.add_user(prompt)
        self.memory.add_opponent(reply)

        return reply
