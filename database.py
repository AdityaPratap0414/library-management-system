import json
from pathlib import Path

DATA_FILE = Path("data/library.json")


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("books", []), data.get("members", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return [], []


def save_data(books, members):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump({"books": books, "members": members}, file, indent=4)
