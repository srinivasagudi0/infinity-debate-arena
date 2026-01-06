# persistent_memory.py

import json
import os

MEMORY_FILE = "arena_memory.json"


def save_last_topic(topic: str):
    data = {"last_topic": topic}
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)


def load_last_topic():
    if not os.path.exists(MEMORY_FILE):
        return None
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)
    return data.get("last_topic")
