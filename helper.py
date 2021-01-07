def filter_vehicles(vehicles, weather):
	"""
		Filter possible vehicles based on weather
	"""
	result = []
	for vehicle in vehicles:
		if weather.lower() in vehicle.can_travel:
			result.append(vehicle)
	
	return result
	
def update_craters_and_traffic_speed(orbits, weather, traffic_speeds):
	"""
		Updates num of craters based on weather
		Updates traffic speed of every orbit
	"""
	
	for i in range(len(orbits)):
		orbits[i].update_craters(weather)
		orbits[i].update_traffic_speed(traffic_speeds[i])

def calculate_time(orbit, vehicle):
	
	# time = distance/speed
	time = orbit.distance/vehicle.max_speed * 60
	# additional time taken to cross each craters
	additional_time = orbit.craters * vehicle.overcome_time
	
	print(orbit.name, vehicle.name)
	print(time+additional_time)
	
	return time + additional_time