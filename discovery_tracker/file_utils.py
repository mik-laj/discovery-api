import json


def save_json(filename, content):
    with open(filename, 'w') as outfile:
        json.dump(content, outfile, indent=" " * 4, sort_keys=True)
