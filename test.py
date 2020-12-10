import unittest
from main import add,subtract,multiply
#comment tests okssssssss
class TestClass(unittest.TestCase):
	def test_add(self):
	    x = 5
	    y = 6
	    expected = 11
	    actual = add(x,y)
	    self.assertEqual(expected, actual) 

	def test_subtract(self):
		x = 10
		y = 5
		expected = 5
		actual = subtract(x,y)
		self.assertEqual(expected, actual) 

	def test_multiply(self):
		x = 10
		y = 5
		expected = 50
		actual = multiply(x,y)
		self.assertEqual(expected, actual) 
