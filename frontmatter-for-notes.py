#!/usr/bin/env python3

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
    return parser.parse_args()


def main(filenames, args):
    """Play with the metadata as you like lol"""
    for filename in filenames:
        note = frontmatter.load(filename)
        note["title"] = os.path.basename(filename).replace(".md", "")
        note["layout"] = "note"
        if args.time:
            note["date"] = args.time
        else:
             note["date"] = datetime.today().strftime('%Y-%m-%d')
        with open(filename, "w") as fp:
            fp.write(frontmatter.dumps(note))


if __name__ == "__main__":
    args = parse_arguments()
    if (not (args.file or args.directory)):
        print("You must enter either a filename or a directory with filenames!")
        sys.exit(1)
    targets = []
    if args.file:
        targets.append(args.file)
    if args.directory:
       targets += [os.path.join(args.directory, x) for x in os.listdir(args.directory) if os.path.isfile(os.path.join(args.directory, x))]
    print(targets)
    main(targets, args)
