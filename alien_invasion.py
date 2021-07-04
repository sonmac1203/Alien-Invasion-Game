import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""Overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game and create game resources"""
		pygame.init()
		self.settings = Settings()
		#self.screen = pygame.display.set_mode( (self.settings.screen_width, self.settings.screen_height) )
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width # Update width
		self.settings.screen_height = self.screen.get_rect().height # Update height
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self) # Make an instance of Ship after the screen has been created
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		""" Start the main loop for the game"""
		while True:
			# Watch for keyboard and mouse movements
			self._check_events()

			# Move the ship
			self.ship.update()

			# Update the bullets
			self._update_bullets()

			# Redraw the screen after each loop passes
			self._update_screen()


	def _check_events(self):
		"""Respond to keypresses and mouse"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Move the ship to the left
			self.ship.moving_left = True
		elif event.key == pygame.K_ESCAPE:
			# Quit the game by pressing escape
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			# Stop
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			# Stop
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet) # Add the new bullet to the group


	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets"""
		# Update the bullet
		self.bullets.update()

		# Get rid of bullets that disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)



	def _update_screen(self): 
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites(): # Loop through all the bullets in the group
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		# Make the most recently drawn screen visible
		pygame.display.flip()


	def _create_fleet(self):
		"""Create the fleet of aliens"""
		# Make an alien
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size # Determine the width and height of an alien
		alien_space_x = self.settings.screen_width - (2*alien_width) # Determine the space available for all aliens
		number_aliens_x = alien_space_x // (2*alien_width) # Calculate the total number of aliens

		# Determine the number of rows of aliens
		ship_height = self.ship.rect.height
		alien_space_y = self.settings.screen_height - (3*alien_height) - ship_height
		number_aliens_y = alien_space_y // (2*alien_height)
		

		for row_number in range(number_aliens_y):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
			

	
	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2*alien_width*alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien_height + 2*alien_height*row_number
		self.aliens.add(alien) # Add the new alien to the group of aliens



if __name__ == '__main__':
	# Make a game instance, and run the game
	ai = AlienInvasion()
	ai.run_game()