class Settings:
	"""A class to store all the settings for Alien Invasion"""

	def __init__(self):
		"""Initialize game settings"""
		self.screen_width = 1000 # Width is 1200 pixels
		self.screen_height = 600 # Height is 800 pixels
		self.bg_color = (230, 230, 230) # Screen's background color

		# Setting of ship's speed
		self.ship_speed = 3
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 5
		self.bullet_width = 20
		self.bullet_height = 20
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 20
		self.fleet_drop_speed_increment = 25
		# fleet_direction of 1 represents right, -1 represents left
		self.fleet_direction = 1



		