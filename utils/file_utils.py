import json
import os

#BUG_DATA_PATH = 'data/bugs.json'

def load_bug_data():
    if os.path.exists('data/bugs.json'):
        with open('data/bugs.json', 'r') as f:
            return json.load(f)
    return {}

def save_bug_data(bug_data):
    with open('data/bugs.json', "w") as f:
        json.dump(bug_data, f, indent=4)