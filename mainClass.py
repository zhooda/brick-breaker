import pygame

class mainClass:
	
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.pos = (self.x, self.y)

		self.xDir = 1
		self.yDir = 1

		self.red = self.green = self.blue = 255
		self.color = (self.red, self.green, self.blue)

		self.surface = pygame.Surface((0,0), pygame.SRCALPHA, 32)
	
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

	def setPos(self, x, y):
		self.x = x
		self.y = y
		self.pos = (self.x, self.y)

	def getXDir(self):
		return self.xDir

	def getYDir(self):
		return self.yDir

	def setXDir(self, xDir):
		self.xDir = xDir

	def setYDir(self, yDir):
		self.yDir = yDir

	def setColor(self, r, g, b):
		self.red, self.green, self.blue = r, g, b
		self.color = (self.red, self.green, self.blue)

	def getPos(self):
		return self.pos

	def getWidth(self):
		return self.surface.get_width()

	def getHeight(self):
		return self.surface.get_height()


class text(mainClass):
	def __init__(self, content, font='Arial', fontSize=24):
		mainClass.__init__(self)
		self.fontFam = font
		self.fontSize = fontSize
		self.content = content

		self.font = pygame.font.SysFont(self.fontFam, self.fontSize)
		self.surface = self.font.render(self.content, 1, self.color)

	def setColor(self, r, g, b):
		mainClass.setColor(r, g, b)
		self.surface = self.font.render(self.content, 1, self.color)

	def getText(self):
		return self.surface

class box(mainClass):
	def __init__(self, width, height, x=0, y=0):
		mainClass.__init__(self, x, y)
		self.width = width
		self.height = height
		self.dim = (self.width, self.height)

		self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
		self.surface.fill(self.color)

	def setColor(self, r, g, b):
		mainClass.setColor(self, r, g, b)
		self.surface.fill(self.color)

	def getBox(self):
		return self.surface

	def autoMove(self, screenDim, xSpd=0, ySpd=0):
		if self.x > screenDim[0] - self.getWidth():
			self.xDir = -1
		if self.x < 0:
			self.xDir = 1
		self.x += self.xDir * xSpd

		if self.y > screenDim[1] - self.getHeight():
			self.yDir = -1
		if self.y < 0:
			self.yDir = 1
		self.y += self.yDir * ySpd

		self.pos = (self.x, self.y)

	def controlMove(self, pressedKeys, screenDim, spd=5):
		if pressedKeys[pygame.K_LEFT]:
			self.x -= spd
		if pressedKeys[pygame.K_RIGHT]:
			self.x += spd

		if self.x > screenDim[0]-self.getWidth():
			self.x = screenDim[0]-self.getWidth()
		if self.x < 0:
			self.x = 0

		self.pos = (self.x, self.y)


def getSpriteCollision(sprite1, sprite2):
	if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <= sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
		return True
	else:
		return False

def getGameOver(sprite1, sprite2):
	if sprite2.getY() > sprite1.getY() + sprite2.getHeight():
		return True
	else:
		return False