#!/usr/bin/env python

import json

json_string = None

with open("addedTweets.json") as f:
    json_string = f.read()
try:
    parsed_json = json.loads(json_string)
    formatted_json = json.dumps(parsed_json, indent=4, sort_keys= True)
    with open("addedTweets.json", "w") as f:
        f.write(formatted_json)
except Exception as e:
    print(repr(e))


