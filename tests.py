'''
t: brick breaker main
a: zeeshan hooda
d: 04/29/2019
'''

import pygame
# from myClass import box, getSpriteCollision
from mainClass import text, box, getSpriteCollision
# loads pygame module commands in the program
pygame.init()

# display variables

# window title
TITLE = 'brick break'

# frames/sec
FPS = 60

WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# colour variables!!!
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

# create the window

screen = pygame.display.set_mode(SCREENDIM) # creates the main surface where other assets are placed
pygame.display.set_caption(TITLE) # updates the window title with TITLE
screen.fill(BLACK) # fills the surface with a colour (erase or clear)

# starts a clock object to measure time
clock = pygame.time.Clock()

testBox = box(80, 40, WIDTH/2 - 40, HEIGHT/2 - 20)
testPlayer = box(150, 20)
testPlayer.setPos(WIDTH/2 - testPlayer.getWidth()/2, HEIGHT - 50)

ball = box(10, 10, WIDTH/2 - 5, testPlayer.getY() - 20)



# --CODE STARTS HERE-- #
running = True
while running:
    # quite important
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # if [x] button is clicked
            running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(BLACK)

    ball.autoMove(SCREENDIM, 5, 5)
    testPlayer.controlMove(pressedKeys, SCREENDIM, 10)
    if getSpriteCollision(ball, testBox):
        ball.setYDir(-ball.getYDir())
    if getSpriteCollision(ball, testPlayer):
        ball.setYDir(-ball.getYDir())
        ball.setY(ball.getY()-1)
    # getSpriteCollision(testPlayer, ball)
    screen.blit(testBox.getBox(), testBox.getPos())
    screen.blit(testPlayer.getBox(), testPlayer.getPos())
    screen.blit(ball.getBox(), ball.getPos())

    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the surface with changes
pygame.quit()

