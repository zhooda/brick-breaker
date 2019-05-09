# imports
import pygame
import random
from settings import *
from sprites import *

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
		
		self.all_sprites = pygame.sprite.Group()
		self.all_bricks = pygame.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		
		

		self.bricks = []

		for i in range(8):
			self.bricks.append(Brick(RED, i*100, 100))
			self.bricks.append(Brick(ORANGE, i*100, 130))
			self.bricks.append(Brick(AMBER, i*100, 160))
			self.bricks.append(Brick(YELLOW, i*100, 190))
			self.bricks.append(Brick(GREEN, i*100, 220))
			self.bricks.append(Brick(BLUE, i*100, 250))
			
		for i in range(len(self.bricks)):
			self.all_sprites.add(self.bricks[i])
			self.all_bricks.add(self.bricks[i])

		self.ball = Ball()
		self.all_sprites.add(self.ball)
		
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
		
		self.all_sprites.update()

		# for brick in self.bricks:
		# 	if self.ball.rect.colliderect(brick.rect):
		# 		self.ball.switchVelY()
		# 		self.bricks.remove(brick)
		# 		self.all_sprites.remove(brick)
		# 		break

		deadblocks = pygame.sprite.spritecollide(self.ball, self.all_bricks, True)
		if len(deadblocks) > 0:
			self.ball.switchVelY()

		if self.ball.rect.colliderect(self.player.rect):
			self.ball.switchVelY()
			if self.ball.vel.x > 0:
				self.ball.vel.x += 0.1
			else:
				self.ball.vel.x -= 0.1
			if self.ball.vel.y > 0:
				self.ball.vel.y += 0.1
			else:
				self.ball.vel.y -= 0.1
		if self.ball.pos.y > self.player.pos.y:
			self.gameActive = False

	# events for the game loop
	def events(self):
		
		for event in pygame.event.get():
			# checks for user closing window
			if event.type == pygame.QUIT:
				if self.gameActive:
					self.gameActive = False
				self.running = False

	def draw(self):
		
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)

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