import json


def save_json(filename, content):
    with open(filename, 'w') as outfile:
        json.dump(content, outfile, indent=" " * 4, sort_keys=True)


def save_text(filename, content):
    with open(filename, 'w') as outfile:
        outfile.write(content)
