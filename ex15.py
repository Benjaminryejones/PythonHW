#Import module argv to take certain arguments
from sys import argv
#Set variable to the argv so we can use it
script = argv
#Prompt the user to specify which file she would like to open
print "What file would you like to open?"
#Set a variable to the input given by the user
filename = raw_input("> ")
#Open the file
txt = open(filename)
#And print its contents
print txt.read()

close(txt)
#Prompt the user to specify another file
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

close(txt_again)