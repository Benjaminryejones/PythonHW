#mystuff = {'apple': "I AM APPLES"}
#print mystuff['apple']
#
#class MyStuff(object):
#
#	def __init__(self):
#		self.tangerine = "And now a thousand years between"
#
#	def apple(self):
#		print "I AM CLASSY APPLES"
#
#thing = MyStuff()
#thing.apple()
#print thing.tangerine
#
## dict style
#mystuff['apple']
#
## module style
#mystuff.apple()
#print mystuff.tangerine
#
## class style
#thing = MyStuff()
#thing.apple()
#print thing.tangerine

######################
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you,"
					"I don't want to get sued",
					"Happy birthday to you."])

bulls_on_parade = Song(["Yes yes yes",
						"This is a future I never wanted."])

randomLyrics = (["Str8", "Hello", "Test"])

test_class = Song(randomLyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

test_class.sing_me_a_song()