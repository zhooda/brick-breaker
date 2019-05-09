# sprite classes
import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((150, 10))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)

		# velocities
		self.pos = vec(WIDTH/2, HEIGHT-30)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

	def update(self):
		self.acc = vec(0, 0)
		pressedKeys = pygame.key.get_pressed()
		if pressedKeys[pygame.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		if pressedKeys[pygame.K_RIGHT]:
			self.acc.x = PLAYER_ACC

		# applies friction
		self.acc += self.vel * PLAYER_FRICTION

		# realistic-ish motion
		self.vel += self.acc
		self.pos += self.vel + (self.acc/2)

		# screen wrapping!!
		if self.pos.x > WIDTH - self.rect.width/2:
			self.pos.x = WIDTH - self.rect.width/2
			self.acc = -self.acc
		if self.pos.x < self.rect.width/2:
			self.pos.x = self.rect.width/2

		self.rect.center = self.pos

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 10))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT-60)

		# velocities
		self.pos = vec(WIDTH/2, HEIGHT-60)
		self.vel = vec(3, -3)

	def update(self):
		if self.pos.x > WIDTH - self.rect.width/2:
			self.vel.x = -self.vel.x
		if self.pos.x < self.rect.width/2:
			self.vel.x = -self.vel.x

		if self.pos.y > HEIGHT - self.rect.height/2:
			self.vel.y = -self.vel.y
		if self.pos.y < self.rect.height/2:
			self.vel.y = -self.vel.y

		self.pos += self.vel
		self.rect.center = self.pos

	def switchVelY(self):
		self.vel.y = -self.vel.y


class Brick(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((100, 30))
		self.image.fill(color)
		self.rect = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.rect.x = self.rect.x
		self.rect.y = self.rect.y