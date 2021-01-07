from initialize import bike, tuktuk, car, orbit1, orbit2

def filter_vehicles(vehicles, weather):
	"""
		Filter possible vehicles based on weather
	"""
	result = []
	for vehicle in vehicles:
		if weather.lower() in vehicle.can_travel:
			result.append(vehicle)
	
	return result
	
def update_craters(orbits, weather):
	"""
		Update num of craters based on weather
	"""
	for orbit in orbits:
		orbit.update_craters(weather)

def calculate_time():
	pass
	
	
inp = "RAINY 45 20"
weather, speed_lim1, speed_lim2 = inp.split(' ')
vehicles = [bike, tuktuk, car]
orbits = [orbit1, orbit2]