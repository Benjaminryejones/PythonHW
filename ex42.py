## Animal is-a object
class Animal(object):
	def __init__(self):
		pass
	def make_sound(self, sound):
		print sound
	pass

## class Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## class Dog has a name
		self.name = name

## class Cat is a Animal
class Cat(Animal):

	def __init__(self, name):
		## class Cat has a name
		self.name = name

## class Person is a object
class Person(object):

	def __init__(self, name):
		## Person has a name
		self.name = name

		# Person has a pet of some kind
		self.pet = None

## class Employee is a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Create a proxy object that delegates method calls to its parent(s) of specified class type
		super(Employee, self).__init__(name)
		## Employee has a salary
		self.salary = salary

## class Fish is a object
class Fish(object):
	pass

## Salmon is a Fish
class Salmon(Fish):
	pass

## Halibut is as Fish
class Halibut(Fish):
	pass

## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has a pet, satan
mary.pet = satan

## frank is a Employee with a 120000 salary
frank = Employee("Frank", 120000)

## frank has a pet, rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()

jimmy = Animal()
#Dog.make_sound("bark")
jimmy.make_sound("dix")
rover.make_sound("growl")