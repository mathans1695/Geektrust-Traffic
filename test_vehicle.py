import unittest
from vehicle import Vehicle

class TestVehicle(unittest.TestCase):
	def setUp(self):
		# Create a sample bike vehicle
		self.bike = Vehicle("bike", 10, 2, ["sunny", "windy"])

	def test_update_speed(self):
		# max_speed should remain unchanged, if traffic speed > max_speed of vehicle
		
		# Record the initial max speed
		initial_speed = self.bike.max_speed
		traffic_speed = 12
		# Run the update speed method of vehicle
		self.bike.update_speed(traffic_speed)
		# Get final max_speed
		final_speed = self.bike.max_speed
		
		# Both speed should equal
		self.assertEqual(initial_speed, final_speed)
		
		# Reset the speed for next test
		self.bike.reset_speed()
		# Speed should reset to original state
		self.assertEqual(self.bike.max_speed, 10)
		
		# max_speed should equal traffic speed, if traffic speed < max_speed of vehicle
		
		traffic_speed = 8
		# Run the update speed method of vehicle
		self.bike.update_speed(traffic_speed)
		# Get final max_speed
		final_speed = self.bike.max_speed
		
		# Both final_speed should equal traffic_speed
		self.assertEqual(final_speed, traffic_speed)
		
if __name__ == "__main__":
	unittest.main()