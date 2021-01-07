class Orbit:
	"""
		Defines an orbit:
		* Pass distance of an orbit 
		* Total number of craters
	"""
	def __init__(self, distance, craters):
		self.distance = distance
		self.craters = craters
		# preserve will have default number of craters before weather hits the orbit
		self.preserve = craters
		
	def update_craters(self, weather):
		"""
			Updates number of craters based on the weather condition
		"""
		if weather.lower() == 'sunny':
			self.craters -= self.craters * 0.10
		elif weather.lower() == 'rainy':
			self.craters += self.craters * 0.20
		else:
			pass
			
	def reset_craters(self):
		"""
			Reset num of craters, after climate becomes normal
		"""
		self.craters = self.preserve