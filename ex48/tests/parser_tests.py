from nose.tools import *
from ex48 import *
from numbers import Number
# from ex48 import parser
import re

def random_test():
	assert_equal(Sentence("I will kill you", "error"))