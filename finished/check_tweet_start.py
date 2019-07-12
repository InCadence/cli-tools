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
        print("Checking File : %s\n" % jsonfile)

        # json_string = None

        count = 1
        with open(jsonfile) as f:
            for line in f:
                try:
                    # the json data
                    data = json.loads(line)

                    # the data in a readable format
                    parsed = json.dumps(data)

                    # the total number of characters parsed
                    total_chars = len(parsed)

                    print("  Checking Line %s : %s" % (count, total_chars))
                except Exception as e:
                    print("ERROR AT LINE %s : %s" % (count, repr(e)))

                count = count + 1


if __name__ == "__main__":
    main()
