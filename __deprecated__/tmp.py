# imports
import pygame
import random

# settings
TITLE = "tmp.py"
WIDTH = 800
HEIGHT = 600
FPS = 60

# colors
RED = (198, 73, 75)
ORANGE = (196, 108, 64)
AMBER = (179, 121, 56)
YELLOW = (162, 161, 54)
GREEN = (75, 159, 76)
BLUE = (67, 77, 197)
GREY = (142, 142, 142)
BLACK = (0, 0, 0)

class Game:
	
	# instantiate game window
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()

		self.running = True

	# reset game variables and start new game
	def newGame(self):
		
		self.sprites = pygame.sprite.Group()
		self.loop()

	# game loop
	def loop(self):
		
		self.gameActive = True
		while self.gameActive:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()


	# kinda self explanatory
	def update(self):
		
		self.sprites.update()

	# events for the game loop
	def events(self):
		
		for event in pygame.event.get():
			# checks for user closing window
			if event.type == pygame.QUIT:
				self.gameActive = False
				self.running = False

	def draw(self):
		
		self.screen.fill(BLACK)
		self.sprites.draw(self.screen)

		pygame.display.flip()

	def getRunning(self):
		return self.running

	def setRunning(self, runStatus):
		self.running = runStatus

	def showStartScreen(self):
		pass

	def showEndScreen(self):
		pass

breakout = Game()
breakout.showStartScreen()

while breakout.getRunning():
	breakout.newGame()
	breakout.showEndScreen()

pygame.quit()