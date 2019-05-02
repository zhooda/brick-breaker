'''
sprite classes
'''

import pygame

class myClass:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.xDir = 1
		self.yDir = 1
		self.pos = (self.x, self.y)
		self.surface = pygame.Surface((0,0), pygame.SRCALPHA, 32)
		self.red = 255
		self.green = 255
		self.blue = 255
		self.color = (self.red, self.green, self.blue)
	def getSurface(self):
		return self.surface
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def setX(self, x):
		self.x = x
		self.pos = (self.x, self.y)
	def setY(self, y):
		self.y = y
		self.pos = (self.x, self.y)
	def getWidth(self):
		return self.surface.get_width()
	def getHeight(self):
		return self.surface.get_height()
	def getPos(self):
		return self.pos
	def setColor(self, color = (0, 0, 0)):
		self.red, self.green, self.blue = color[0], color[1], color[2]
		self.color = (self.red, self.green, self.blue)
	def setPos(self, x, y):
		self.x = x
		self.y = y
		self.pos = (self.x, self.y)
	def setDirs(self, xDir, yDir):
		self.xDir = xDir
		self.yDir = yDir
	def switchDirs(self):
		self.xDir = -self.xDir
		self.yDir = -self.yDir
	def getDirs(self):
		return (self.xDir, self.yDir)
	def controlMove(self, pressedKeys, screenDim, spd=5):
		if pressedKeys[pygame.K_a]:
			self.x -= spd
		if pressedKeys[pygame.K_d]:
			self.x += spd
		if pressedKeys[pygame.K_w]:
			self.y -= spd
		if pressedKeys[pygame.K_s]:
			self.y += spd

		if self.x > screenDim[0]-self.width:
			self.x = screenDim[0]-self.width
		if self.x < 0:
			self.x = 0
		if self.y > screenDim[1]-self.height:
			self.y = screenDim[1]-self.height
		if self.y < 0:
			self.y = 0

		self.pos = (self.x, self.y)


	def autoMove(self, screenDim, xSpd=0, ySpd=0):

		if self.x > screenDim[0]-self.surface.get_width():
			self.xDir = -1
		if self.x < 0:
			self.xDir = 1
		self.x += self.xDir*xSpd

		if self.y > screenDim[1]-self.surface.get_height():
			self.yDir = -1
		if self.y < 0:
			self.yDir = 1

		self.y += self.yDir*ySpd
		self.pos = (self.x, self.y)

class text(myClass):
	def __init__(self, content, font='Arial', fontSize=24):
		myClass.__init__(self)
		self.fontFam = font
		self.fontSize = fontSize
		self.font = pygame.font.SysFont(self.fontFam, self.fontSize)
		self.content = content
		self.surface = self.font.render(self.content, 1, self.color)
	def setColor(self, color = (0, 0, 0)):
		myClass.setColor(self, color)
		self.surface = self.font.render(self.content, 1, self.color)
	def getText(self):
		return myClass.getSurface(self)

class box(myClass):
	def __init__(self, width, height, x=0, y=0):
		myClass.__init__(self, x, y)
		self.width = width
		self.height = height
		self.dim = (self.width, self.height)
		self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
		self.surface.fill(self.color)
	def setColor(self, color = (0,0,0)):
		myClass.setColor(self, color)
		self.surface.fill(self.color)
	def getBox(self):
		return myClass.getSurface(self)


def getSpriteCollision(sprite1, sprite2):
	if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <= sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
		return True
	else:
		return False

class mySprite(myClass):
	def __init__(self, philName):
		myClass.__init__(self)
		self.surface = pygame.transform.scale(pygame.image.load(philName).convert_alpha(), (100, 143))
## incorporate auto move and keyboard into class file
## incorporate specific methods into text and box classes
## incorporate at least one specific method into text or box that overrides a parent method (ie. set color)
## 