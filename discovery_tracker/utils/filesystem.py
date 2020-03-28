import json
import os


def save_json(filename: str, content):
    with open(filename, 'w') as outfile:
        json.dump(content, outfile, indent=" " * 4, sort_keys=True)


def load_json(filename: str):
    with open(filename, 'r') as outfile:
        return json.load(outfile)


def save_text(filename: str, content: str):
    with open(filename, 'w') as infile:
        infile.write(content)


def load_text(filename: str) -> str:
    if not os.path.exists(filename):
        return ""

    with open(filename, 'r') as infile:
        return infile.read()
