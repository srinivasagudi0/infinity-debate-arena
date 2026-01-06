# memory.py

class DebateMemory:
    def __init__(self, max_turns: int = 6):
        self.max_turns = max_turns
        self.history = []

    def add_user(self, content: str):
        self.history.append({"role": "user", "content": content})
        self._trim()

    def add_opponent(self, content: str):
        self.history.append({"role": "assistant", "content": content})
        self._trim()

    def get(self):
        return self.history

    def _trim(self):
        # Keep only the most recent turns
        excess = len(self.history) - (self.max_turns * 2)
        if excess > 0:
            self.history = self.history[excess:]
