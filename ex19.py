def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket. \n"

#Can give function numbers directly
cheese_and_crackers(20, 30)

#Or you can use variables from our script
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

#Can also do math
cheese_and_crackers(10 + 20, 5 + 3)

#Can combine variables and math
cheese_and_crackers(10 + amount_cheese, amount_crackers + 55)