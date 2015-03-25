i = 0
numbers = []

def while_loop(start, end):
	for dix in range(start, end):
		if dix == end:
			break
		else:
			print "At the top i is %d" % dix
			numbers.append(dix)
			print "Numbers now: ", numbers
			print "At the bottom i is %d" % dix

#while i < 6:
#	print "At the top i is %d" % i
#	numbers.append(i)
#	i = i + 1
#	print "Numbers now: ", numbers
#	print "At the bottom i is %d" % i

while_loop(1, 6)

print "The numbers: "

for num in numbers:
	print num