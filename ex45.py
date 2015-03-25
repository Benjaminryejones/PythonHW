import sys
from random import randint
import time
import math
import ex45_events

case_count = 0

def timer():
	"""15-second timer function. Called in all of the decision moments."""
	time_count = 15
	while True:
		time.sleep(1)
		time_count -= 1
		print "%d seconds remain." % time_count

		if time_count <= 0:
			print "Time's up!"
			break

def case_counter():
	"""Global case counter."""
	global case_count
	case_count += 1

def game_init():

	print "Welcome to King's Decision!"
	print "To read the game description and a brief tutorial, enter 't'."
	print "Otherwise, enter 's' to begin."

	user_input = raw_input("> ")

	if user_input == 't':
		tutorial()
	elif user_input == 's':
		game_start()
	else:
		print "Invalid input, reinitializing."
		game_init()

def tutorial():
	"""Print out a brief game description and tutorial. After the user presses a key, the game will begin."""
	print "King's Decision puts you in the position of a king forced to make quick choices."
	print "You will be presented with a number of random situations and given a number of "
	print "choices to choose from. You will have 15 seconds to make a snap decision; if you "
	print "fail to come to a decision, you will automatically choose to behead the person presenting "
	print "the case, much to the chagrin of your court and subjects. If you do this twice, the people "
	print "will revolt and kill you."
	print "\n"
	print "The goal is to come to prudent, informed, and honorable decisions. Bad decisions will"
	print "bring consequences, such as growing unrest among the people. If you are able to make"
	print "good decisions five times in a row, you will win the title of 'the Great', and win the game."
	print "Best of luck to you, the king!"
	time.sleep(5)
	raw_input("Press any key to begin the game.")
	game_start()

def case_array_maker():
	"""Create an array with random, unique values 1-10. Used as input to select cases."""
	x = []
	# x=[randint(1,10) for p in range(1,10)] # Can repeat array values (undesirable)
	while len(x) < 10:
		t = randint(1,10)
		if t not in x:
			x.append(t)
		else:
			pass

	return x

def game_start():
	print "Game start!"
	case_array = case_array_maker()
	for x in range(0,9):
		case_selector(case_array[x])
	else:
		print "Unexpected error, reinitializing"
		game_init()

def case_selector(case_number):
	for x in range(0,9):
		if x == case_number:
			call_case = getattr(ex45_events, 'case' + str(x))
			call_case()
		else:
			pass

#######
#game_init()