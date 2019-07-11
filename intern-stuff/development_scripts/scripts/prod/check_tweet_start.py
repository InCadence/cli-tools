#!/usr/bin/env python

# This script goes through the addedTweets.json 
# files and validates and formats the data.
# Enter the file name surrounded by quotes ("......")

import json
def main():

    json_string = None
    jsonfile = str(input("Please enter the file name: "))
    while True:
        with open(jsonfile) as f:
            json_string = f.read()
        try:
            parsed_json = json.loads(json_string)
            formatted_json = json.dumps(parsed_json, indent=4, sort_keys= True)
            with open(jsonfile, "w") as f:
                f.write(formatted_json)
            print("looks good")
        except Exception as e:
            print(repr(e))
            break

if __name__ == "__main__":
    main



