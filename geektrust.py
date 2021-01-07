from helper import filter_vehicles, update_craters_and_traffic_speed, calculate_time

from initialize import vehicles, orbits


def main():
	inp = "SUNNY 12 10"
	weather, traffic_speed1, traffic_speed2 = inp.split(' ')
	traffic_speeds = [int(traffic_speed1), int(traffic_speed2)]
	
	selected = filter_vehicles(vehicles, weather)
	update_craters_and_traffic_speed(orbits, weather, traffic_speeds)
	
	suitable_vehicle = None
	suitable_route = None

	time = 10000

	for orbit in orbits:
		for vehicle in selected:
			vehicle.update_speed(orbit.traffic_speed)
			
			calc_time = calculate_time(orbit, vehicle)
			if calc_time < time:
				time = calc_time
				suitable_vehicle = vehicle.name
				suitable_route = orbit.name
				
			vehicle.reset_speed()
			
	print(suitable_vehicle.upper(), suitable_route.upper())

if __name__ == "__main__":
	main()