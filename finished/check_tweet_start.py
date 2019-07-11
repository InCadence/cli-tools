#!/usr/bin/env python

# This script goes through the addedTweets.json
# files and validates and formats the data.
# Enter the file name surrounded by quotes ("......")

import json
import sys


def main():

    # gets json file passed in from the user
    args = sys.argv
    if len(args) != 2:
        # if we got here then they either entered too many args or not enough
        print("You must supply a json file to check")

        # time to bail
        sys.exit()
    else:
        # ok, looking good. let's remove some files
        jsonfile = sys.argv[1]
        print("Checking File : %s" % jsonfile)

        # json_string = None
        while True:
            with open(jsonfile) as f:
                json_string = f.read()
            try:
                parsed_json = json.loads(json_string)
                formatted_json = json.dumps(parsed_json, indent=4, sort_keys=True)
                with open(jsonfile, "w") as f:
                    f.write(formatted_json)
                print("looks good")
            except Exception as e:
                print(repr(e))
                break


if __name__ == "__main__":
    main()
