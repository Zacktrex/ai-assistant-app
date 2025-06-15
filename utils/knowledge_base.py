import json
from difflib import get_close_matches

KB_PATH = "kb/knowledge_base.json"

def load_kb():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def search_kb(query, kb_data):
    questions = list(kb_data.keys())
    matches = get_close_matches(query, questions, n=1, cutoff=0.6)
    return kb_data[matches[0]] if matches else None
