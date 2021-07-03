import pygame

from settings import Settings

class Ship:
	"""A class to control the ship"""
	
	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position"""
		self.screen = ai_game.screen # Assign the screen to an attribute of ship
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect() # Access the screen's rect attribute
		


		# Load the ship's image and get its rect
		self.image = pygame.image.load('images/ship.bmp') # Load the image
		self.rect = self.image.get_rect() 

		# Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the ship's horizontal position
		self.x = float(self.rect.x)


		# Movement flag
		self.moving_right = False
		self.moving_left = False


	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update rect object from self.x
		self.rect.x = self.x


	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)