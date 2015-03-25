def start():
	print """You awake, finding yourself in a dark room.
	In front of you lies a passageway.
	Without really knowing why, you walk towards the opening...
	"""
	print "Press any key to continue..."
	raw_input("> ")
	hallway()

def concert():
	print """As you continue walking, you begin to hear some faint sounds.
	These sounds grow in volume, until you can distinctly make out beats and glitch.
	You arrive at a massive concert hall, and just as you enter the crowd a mega-dub-dub drop begins.
	For the rest of your life you dance and drop.
	"""
	exit(0)

def choice(choice1, choice2):
	print "So, what do you do? %s or %s?" % (choice1, choice2)
	user_choice = raw_input("> ")

	if user_choice == choice1:
		return 1
	elif user_choice == choice2:
		return 2
	else:
		print "You wallow in indecision, resorting to making arbitrary attempts at action. You die, confused."

def hallway():
	print "You enter a long hallway. After walking for what feels like hours, you reach a fork in the path."
	print "One path goes left; the other right"
	user_decision = choice("left", "right")
	if user_decision == 1:
		concert()
	else:
		portal()

def portal():
	print "You head down a short passageway before seeing something astounding: a portal."
	print "Producing a screeching sound while slowly seeming to suck you in, the portal calls to you."
	user_decision = choice("gaze into the portal", "jump into the portal")

	if user_decision == 1:
		print "You gaze into the portal, and suddenly..."
		harem()
	else:
		print "You jump into the portal. You feel yourself being ripped apart, when suddenly..."
		start()

def harem():
	print "You land in what can only be described as a tropical paradise."
	print "Beautiful trees, hot weather, beaches, and most importantly, hot babes are everywhere!"
	print "You live out you days peacefully..."
	exit(0)