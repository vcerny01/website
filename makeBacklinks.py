import os
import sys
import re
import json

LINK_PATTERN = re.compile("\[\[(.*?)\]\]")
BACKLINKS = {}
TARGET_DIR = sys.argv[1]
OUTPUT_DIR = sys.argv[2]

def parse_file(path_to_file, name):
	file = open(path_to_file, "r")
	links = re.findall(LINK_PATTERN, file.read())
	links = [x.split("|")[0] for x in links]
	if name in links:
		return True

def urlize(name_string):
	# name_string = name_string.lower().replace(" ", "-")
	name_string = name_string.replace(TARGET_DIR, "").replace(".md", "")
	if name_string[0] == "/":
		name_string = name_string.replace("/", "", 1)
	return name_string

def parse_dir_backlinks(directory, name):
	links = []
	for filename in os.listdir(directory):
		full_path = os.path.join(directory, filename)
		if os.path.isdir(full_path):
			links += parse_dir_backlinks(full_path, name)
		elif ".md" in full_path:
			if parse_file(full_path, name):
				links += [urlize(full_path)]
	return links	

def parse_dir(directory):
	for filename in os.listdir(directory):
		print(filename)
		name = filename.replace(".md", "")
		full_path = os.path.join(directory, filename)
		if os.path.isdir(full_path):
			parse_dir(full_path)
		elif ".md" in filename:
			print("Searching backlinks for file " + full_path)
			BACKLINKS[urlize(full_path)] = parse_dir_backlinks(directory, name)

parse_dir(TARGET_DIR)
jsonfp = open(os.path.join(OUTPUT_DIR, "backlinks.json"), "w")
json.dump(BACKLINKS, jsonfp, indent=4)