class Vehicle:
	"""
		Definition of vehicle:
		Pass properties of a vehicle as parameters to init
		* max_speed of vehicle
		* overcome_time prop is the minimum time taken by the vehicle to cross a crater in megamiles
		* can_travel should be list of weather, the vehicle can handle
	"""
	def __init__(self, name, max_speed, overcome_time, can_travel):
		self.name = name
		self.max_speed = max_speed
		self.overcome_time = overcome_time
		self.can_travel = can_travel