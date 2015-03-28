from numbers import Number
import re

direction_words = ("north", "south", "east", "west", "up", "down", "left", "right")
verb_words = ("go", "stop", "kill", "eat")
stop_words = ("the", "in", "of", "at", "from", "it")
noun_words = ("door", "bear", "princess", "cabinet")
number_words = (r"\d")

# Returns value.
def scan(words):
	sentence = []
	result = words.split()

	direction_words = ("north", "south", "east", "west", "up", "down", "left", "right")
	verb_words = ("go", "stop", "kill", "eat")
	stop_words = ("the", "in", "of", "at", "from", "it")
	noun_words = ("door", "bear", "princess", "cabinet")
	number_words = (i for i in range(10))

	for word in result:

		if word in direction_words:
			sentence.append(('direction', word))
		elif word in verb_words:
			sentence.append(('verb', word))
		elif word in stop_words:
			sentence.append(('stop', word))
		elif word in noun_words:
			sentence.append(('noun', word))
		elif word.isdigit():
			sentence.append(('number', convert_number(word)))
		elif convert_number(word) == None:
			sentence.append(('error', word))
		else:
			sentence.append(('number', word))

	return sentence

def convert_number(s):
	try:
		return int(s)
	except ValueError or TypeError:
		return None


