#Going to set up some variables and set the values for said variables here
cars = 100.
space_in_a_car = 4.
drivers = 30.
passangers = 90.
#Doing some variable calculations that we will use later.
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passangers_per_car = passangers / cars_driven

#Printing some text about the current state of our taxi cab company
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passangers, "to carpool today."
print "We need to put about", average_passangers_per_car, "in each car."

print cars / drivers