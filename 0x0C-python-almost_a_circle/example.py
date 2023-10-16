#!/usr/bin/python3
import json
with open("data.json", "r") as f:
    data = json.dump(f)

print(json.loads(data))
