from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "When you see the name of this script, what do you think?"
answer = raw_input()

print "Yes, I too think of %r" % (answer)

