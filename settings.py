import json

try:
    settings = json.load(open("settings.json", "r"))
except FileNotFoundError:
    settings = {
        "invertScreen": 5,
        "blockInput": 5
    }
    json.dump(settings, open("settings.json", "w"))