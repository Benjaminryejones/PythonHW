name = 'Rye Jones'
age = 23
height = 72 # Inches
weight = 155 / 2.2 # kg
eyes = 'Green'
teeth = 'White'
hair = "Blonde"

print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "He's %g kg heavy." % weight
print "Actually that's not too heavy -- he's even been losing weight lately."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)