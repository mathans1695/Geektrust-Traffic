import sys

from helper import filter_vehicles, update_craters_and_traffic_speed, calculate_time
from initialize import vehicles, orbits

def main():
	
	# Read input file and store it in inp
	with open(sys.argv[1], 'r') as f:
		inp = f.read()
	
	# Process the inputs and store it corresponding variables
	inp = [i.strip() for i in inp.split(' ')]
	weather, traffic_speed1, traffic_speed2 = inp
	traffic_speeds = [int(traffic_speed1), int(traffic_speed2)]
	
	# Select vehicle that can handle the current weather condition
	selected = filter_vehicles(vehicles, weather)
	
	# Update number of craters based on weather condition
	# And add traffic speed property to each orbits
	update_craters_and_traffic_speed(orbits, weather, traffic_speeds)
	
	suitable_vehicle = None
	suitable_route = None
	
	# Set time to some big arbitary number
	time = 10000

	# Iterate through every orbits and calculate time taken for travel
	for orbit in orbits:
		for vehicle in selected:
			
			# update max_speed based on traffic speed
			vehicle.update_speed(orbit.traffic_speed)
			
			# calculate time taken for travel
			calc_time = calculate_time(orbit, vehicle)
			
			# Update vehicle that takes less time to travel on particular route
			if calc_time < time:
				time = calc_time
				suitable_vehicle = vehicle.name
				suitable_route = orbit.name
				
			# Reset the speed to its original speed
			vehicle.reset_speed()
	
	return (suitable_vehicle.upper(), suitable_route.upper())

if __name__ == "__main__":
	print(' '.join(main()))