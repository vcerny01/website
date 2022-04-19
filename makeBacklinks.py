import os
import sys
import re
import json

LINK_PATTERN = re.compile("\[\[(.*?)\]\]")


links = {}
for filename in os.listdir(sys.argv[1]):
	file = open(filename, "r")
	name = filename.lower().replace(".md", "").replace(" ", "-")
	content = file.read()
	linked_notes = re.findall(LINK_PATTERN, content)
	links[name] = linked_notes

jsonfp = open("backlinks.json", "w")
json.dump(links, jsonfp, indent=4)