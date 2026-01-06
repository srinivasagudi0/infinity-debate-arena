# ⚡ Infinity Debate Arena

A Stark‑inspired **Human vs AI debate game** built around a **single OpenAI NLU engine**. The project is designed as a logic‑first arena where arguments matter, persistence exists, and quitting is a conscious decision.

> No simulations. No shortcuts. Only logic.

---

## 🧠 What is Infinity Debate Arena?

Infinity Debate Arena is a command‑line debate game where a human user engages in a structured argument against an AI agent. The system is intentionally minimal:

* One human
* One AI agent
* One reasoning engine

There are no judges, no multiple models, and no hidden decision‑makers. The outcome is driven by rules, persistence, and player choice.

---

## 🎮 Core Gameplay

* Choose a debate topic (e.g., `AI vs Humanity` or a free‑form question)
* Select which side you will argue
* Pick a difficulty level
* Engage in turn‑based argument rounds
* Resign or exit at any time

The debate continues until you resign, exit, or the arena reaches its conclusion.

---

## 🏳️ Commands

These commands are available at **any time** during gameplay:

* **`resign`** — Forfeit the debate honorably
* **`exit`** — Save the current state and disengage

Exiting does **not** end the debate permanently. You may resume later.

---

## 💾 Persistent Memory

Infinity Debate Arena features long‑term memory:

* The debate state is saved automatically
* If the program stops, the debate can be resumed on the next launch
* On startup, the system asks whether to continue the previous debate

This makes the arena behave like a real game rather than a disposable chat session.

---

## ⚙️ Architecture Philosophy

* **Single Engine**: All game logic lives in `main.py`
* **Single AI Brain**: One OpenAI NLU call path
* **No Utilities**: No helper abstractions that hide behavior
* **Deterministic Rules**: Wins and exits are rule‑based, not AI‑judged

The design prioritizes transparency, debuggability, and long‑term extensibility.


---

## 🚀 Goals

* Teach structured reasoning through play
* Create a resumable, logic‑first debate experience
* Serve as a clean foundation for future expansions (UI, scoring, multiplayer)

---

## 📌 Status

This project is in **active development**. The core loop and architecture are intentionally kept minimal to preserve clarity and control.

---


