import unittest
from orbit import Orbit

class TestOrbit(unittest.TestCase):
	def setUp(self):
		# Create an Orbit instance
		self.orbit = Orbit("orbit1", 18, 20)
		
	def test_update_traffic_speed(self):
		# Initially, traffic speed property will be None
		
		# Should change traffic speed with passed speed
		self.orbit.update_traffic_speed(15)
		# Assert
		self.assertEqual(self.orbit.traffic_speed, 15)
		
	def test_update_craters(self):
		# Should change the num of craters based on weather condition
		
		# Should increase by 20%, if weather is rainy
		self.orbit.update_craters('RAINY')
		# Assert
		self.assertEqual(self.orbit.craters, 24)
		
		# Reset the num of craters for next test
		self.orbit.reset_craters()
		# Assert
		self.assertEqual(self.orbit.craters, 20)
		
		# Should decrease by 10%, if weather is sunny
		self.orbit.update_craters('SUNNY')
		# Assert
		self.assertEqual(self.orbit.craters, 18)
		
		# Reset the craters for next test
		self.orbit.reset_craters()
		
		# Should remain unchanged, if weather is windy
		self.orbit.update_craters('WINDY')
		# Assert
		self.assertEqual(self.orbit.craters, 20)
	
	
if __name__ == "__main__":
	unittest.main()