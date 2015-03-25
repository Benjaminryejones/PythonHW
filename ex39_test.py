import hashmap
def line():
	print '-' * 10

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Miami')

hashmap.set(cities, 'NY', 'NYC')
hashmap.set(cities, 'OR', 'Portland')

line()
##print "NY state has: %s" % hashmap.get(cities, 'NY')
#Instead of printing this line, we can use an assertion to double check if the expected
#value is being returned.
assert hashmap.get(cities, 'NY') == 'NYC'
print "OR state has: %s" % hashmap.get(cities, 'OR')

line()
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

line()
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

line()
hashmap.list(cities)

line()
hashmap.list(cities)

line()
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas"

#Default values using ||= with the nil result
#Can I do it on one line?
line()
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

line()
hashmap.dump(states)
