## write emogi in a file.

import random
import os
import datetime


def generate_tags():
	tags = []
	# generate random number of tags.
	for i in range(1, random.randint(1, 5)):
		tags.append("tag-" + str(i))
	return tags


def generate_content(count=100):
	for i in range(1, count):
		# create folder.
		# array of emogi unicode.
		emogi = ['🫣', '👀', '😵‍💫', '🤯', '🤗', '🤔', '🤓', '🤠', '🤑', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠']
		# get random emogi.
		random_emogi = random.choice(emogi)
		# create folder.
		folder_name = "emogi-" + str(i)
		os.mkdir(folder_name)
		# create file.
		file_name = folder_name + "/emogi.md"
		file = open(file_name, "w", encoding="utf-8")
		# write emogi in file.
		file.write(random_emogi)
		# write tags in file.
		file.write("tags: " + str(generate_tags()))
		# write date in file.
		file.write("date: " + str(datetime.datetime.now()))
		# close file.
		file.close()


generate_content()