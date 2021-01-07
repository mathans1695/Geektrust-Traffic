import unittest, sys

from geektrust import main

class TestGeekTrust(unittest.TestCase):
	def test_main(self):
		# Provide path to input file, while excecuting the program
		
		# Should return tuple 'CAR' and 'ORBIT2', if condition satisfied
		sys.argv.append('data.txt')
		result = main()
		# Assert
		self.assertEqual(result[0], "CAR")
		self.assertEqual(result[1], "ORBIT2")
	
if __name__ == "__main__":
	unittest.main()