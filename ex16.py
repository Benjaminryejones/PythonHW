from sys import argv

script, filename = argv

print "We're going to erase %r." #filename
print "If you don't want to do that, hit cntl + c."
print "If you do want that, press return"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask for three lines"

line1 = raw_input("line one:")
line2 = raw_input("line two:")
line3 = raw_input("line three:")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3)

print "And finally, we close it"

target.close()