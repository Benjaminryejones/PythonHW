def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d - %d" % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d - %d" % (a, b)
	return a / b

age = add(20, 3)
height = subtract(75, 3)
weight = multiply(80, 2)
iq = divide(300, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "This puzzle becomes ", what