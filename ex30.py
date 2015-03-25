people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide"

if trucks > cars:
	print "stuff"
elif trucks < cars:
	print "Maybe we can take the trucks"
else:
	print "We still can't decide"

if people > trucks:
	print "OK, trucks it is"
else:
	print "Fine, let's just stay home"