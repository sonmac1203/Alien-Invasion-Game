class Settings:
	"""A class to store all the settings for Alien Invasion"""

	def __init__(self):
		"""Initialize game settings"""
		self.screen_width = 1000 # Width is 1200 pixels
		self.screen_height = 600 # Height is 800 pixels
		self.bg_color = (230, 230, 230) # Screen's background color

		# Setting of ship's speed
		self.ship_speed = 1.5

		# Bullet settings
		self.bullet_speed = 5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3



		