#!/usr/bin/env python3

# Might be good to use along with [rmdc](https://github.com/vcerny01/rndc)

import os
import sys
import argparse
from datetime import datetime
import frontmatter


def parse_arguments():
    """Parse commadn line arguments"""
    parser = argparse.ArgumentParser(description="Add frontmatter to files")
    parser.add_argument("-f", "--file", type=str, help="Target filename", required=False)
    parser.add_argument("-d", "--directory", type=str, help="Target directory", required=False)
    parser.add_argument("-t", "--time", type=str, help="Date for the note", required=False)
    parser.add_argument("-s", "--series", type=str, help="Series of the note", required=True)
    return parser.parse_args()


def urlize(name: str):
    """Urlize string like Hugo does"""
    return name.lower().replace(" ", "-")


def main(filenames, arguments):
    """Play with the metadata as you like lol"""
    for filename in filenames:
        note = frontmatter.load(filename)
        note["title"] = os.path.basename(filename).replace(".md", "")
        note["layout"] = "note"
        if arguments.time:
            note["date"] = arguments.time
        else:
            note["date"] = datetime.today().strftime("%Y-%m-%d")
        if arguments.series:
            note["series"] = arguments.series
        with open(urlize(filename), "w") as fp:
            fp.write(frontmatter.dumps(note))
        if urlize(filename) != filename:
            os.remove(filename)


if __name__ == "__main__":
    args = parse_arguments()
    if not (args.file or args.directory):
        print("You must enter either a filename or a directory with filenames!")
        sys.exit(1)
    targets = []
    if args.file:
        targets.append(args.file)
    if args.directory:
        targets += [
            os.path.join(args.directory, x)
            for x in os.listdir(args.directory)
            if os.path.isfile(os.path.join(args.directory, x))
        ]
    print(targets)
    main(targets, args)
