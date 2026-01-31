import os
import json
from typing import List, Dict

KB_STATE_FILE = "data/vectorstore/kb_state.json"


def save_kb_state(sources: List[Dict]):
    os.makedirs("data/vectorstore", exist_ok=True)
    with open(KB_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(sources, f, indent=2, ensure_ascii=False)


def load_kb_state() -> List[Dict]:
    if not os.path.exists(KB_STATE_FILE):
        return []
    with open(KB_STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
