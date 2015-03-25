#Initializer function that creates a hashmap. This creates a list, aMap, with num_buckets
#amount of lists inside of it.
def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets"""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

#Use the hash function to convert a string into an int. Then use the modulus to get the remainder
#of the hash reult and the current length of the aMap hash list. This will result in a unique key.
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to an index
	for the aMap's buckets"""
	return hash(key) % len(aMap)

#Use the hash_key function to find the bucket possibly containing the key.
def get_bucket(aMap, key):
	"""Given a bucket, find the bucket where it would go"""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

#Uses get_bucket to find the bucket a key could be in, and then checks all the values in said
#bucket to check for a match between the key and the value. If successful, it returns the index,
#key, and value for the bucket; if not, it returns some default values.
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None) when not found.
	"""
	bucket = get_bucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v

	return -1, key, default

#Uses get_slot to find the index, key, and value for a bucket and then returns the bucket's value.
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default"""
	i, k, v = get_slot(aMap, key, default=default)
	return v

#Sees if there is a current value in the relevant bucket. If so, it gets replaced with a new
#key-value pair; if not, the key-value pair gets appended to the list.
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value"""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i >= 0:
		#The key exists, replace it
		bucket[i] = (key, value)
	else:
		#The key does not exist, append to create it
		bucket.append((key, value))

#Searches through the hash buckets to see if the key-value pair in question exists.
#If so, it gets deleted from the list.
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

#Print out the key-value pairs contained in our hash map.
def list(aMap):
	"""Prints out what is in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v

#A debug function that prints the contents of every bucket. ??
def dump(aMap):
	"""Prints out every bucket in the Map."""
	for bucket in aMap:
		for k, v in bucket:
			print k, v