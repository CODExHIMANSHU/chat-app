import json
import os

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)
    print("Saved to", filename)

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

save_data("server/database/messages.json", [
    {"sender": "Himanshu", "text": "Hello!"},
    {"sender": "Sarah", "text": "Hi there!"}
])

data = load_data("server/database/messages.json")
print("Loaded:", data)