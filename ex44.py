### Implicit Inheritance Example
# class Parent(object):
# 	def implicit(self):
# 		print "PARENT implicit()"
#
# class Child(Parent):
# 	pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()

######################################
### Override Explicitly Inheritance
# class Parent(object):
# 	def override(self):
# 		print "PARENT override()"
#
# class Child(Parent):
#
# 	def override(self):
# 		print "CHILD override()"
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()

######################################
### Alter Before or After
# class Parent(object):
#
# 	def altered(self):
# 		print "PARENT altered()"
#
# class Child(Parent):
#
# 	def altered(self):
# 		print "CHILD, BEFORE PARENT altered()"
# 		# If you still want to access the Parent function,
# 		# you can do so by calling "super" on the class.
# 		super(Child, self).altered()
# 		print "CHILD, AFTER PARENT altered()"
#
# dad = Parent()
# son = Child()
#
#dad.altered()
#son.altered()

######################################
# ## Mega combo
# class Parent(object):
#
# 	def override(self):
# 		print "PARENT override()"
#
# 	def implicit(self):
# 		print "PARENT implicit()"
#
# 	def altered(self):
# 		print "PARENT altered()"
#
# class Child(Parent):
#
# 	# This will override the Parent override function
# 	def override(self):
# 		print "CHILD override()"
#
# 	# This will do a Before and After alteration (super calls the parent function)
# 	def altered(self):
# 		print "CHILD, BEFORE altered()"
# 		super(Child, self).altered()
# 		print "CHILD, AFTER altered()"
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# # Will implicitly inheiret the Parent function
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()

######################################
### A common use of super(type, self)
# class Child(Parent):
#
# 	def __init__(self, stuff):
# 		# Set some variables in the Child init before initializing the Parent init function
# 		self.stuff = stuff
# 		super(Child, self).__init__()

######################################
## An alternative: Composition
class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE altered()"
		self.other.altered()
		print "CHILD, AFTER altered()"

son = Child()

son.implicit()
son.override()
son.altered()