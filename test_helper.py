import unittest

from helper import filter_vehicles, calculate_time
from orbit import Orbit
from vehicle import Vehicle

class TestHelper(unittest.TestCase):
	def setUp(self):
		# create three instance of vehicle
		self.bike = Vehicle("bike", 10, 2, ["sunny", "windy"])
		self.tuktuk = Vehicle("tuktuk", 12, 1, ["sunny", "rainy"])
		self.car = Vehicle("car", 20, 3, ["sunny", "rainy", "windy"])

		# create one instance of orbit
		self.orbit = Orbit("orbit1", 18, 20)

		self.vehicles = [self.bike, self.tuktuk, self.car]

	def test_filter_vehicles(self):
		# Should return list of selected vehicles based on weather condition
		
		# Should return tuktuk and car vehicles, if weather is 'rainy'
		selected = filter_vehicles(self.vehicles, 'RAINY')
		# Assert
		self.assertEqual(selected[0].name, 'tuktuk')
		self.assertEqual(selected[1].name, 'car')
		
	def test_calculate_time(self):
		# Should time taken by a vehicle to travel a particular orbits
		time = calculate_time(self.orbit, self.bike)
		# Assert
		self.assertEqual(time, 148.0)

if __name__ == "__main__":
	unittest.main()