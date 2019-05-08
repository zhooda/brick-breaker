'''
t: brick breaker main
a: zeeshan hooda
d: 04/29/2019
'''

import pygame
# from myClass import box, getSpriteCollision
from mainClass import text, box, getSpriteCollision, getGameOver
# loads pygame module commands in the program
pygame.init()

# display variables

# window title
TITLE = 'TESTS'

# frames/sec
FPS = 30

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


testPlayer = box(150, 20)
testPlayer.setPos(WIDTH/2 - testPlayer.getWidth()/2, HEIGHT - 50)

ball = box(10, 10, WIDTH/2 - 50, testPlayer.getY() - 20)

brick = box(100, 50, 10, HEIGHT/2)

brickArray = []

def getBrickCollision(ball, brick):
    if getSpriteCollision(ball, brick):
        if brick.getY() <= ball.getY() <= brick.getY() + brick.getHeight() - ball.getHeight():
            ball.setXDir(-ball.getXDir())
        #     if brick.getY() - ball.getHeight() == ball.getY():
        #         ball.setYDir(1)
        #     if ball.getY() == brick.getY() + brick.getHeight() + ball.getHeight():
        #         ball.setYDir(-1)
        # if brick.getX():
        #     ball.setYDir(-ball.getYDir())
        else:
            ball.setYDir(-ball.getYDir())
        brick.setPos(-100, -100)

def testLevel(height):
    for i in range(7):
        brickArray.append(box(100, 50, 5 + (115*i), height))


# brick array
# for i in range(8):
#     brickArray.append(box(100, 40))

testLevel(100)
testLevel(165)
testLevel(230)

# --CODE STARTS HERE-- #
running = True
while running:
    # quite important
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # if [x] button is clicked
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pressedKeys = pygame.key.get_pressed()
    screen.fill(BLACK)


    ball.autoMove(SCREENDIM, 7, 7)
    # testPlayer.controlMove(pressedKeys, SCREENDIM, 10)
    testPlayer.setPos(ball.getX()-testPlayer.getWidth()/2, testPlayer.getY())
    # for i in range(len(brickArray)):
    #     if getSpriteCollision(ball, brickArray[i]):
    #         ball.setYDir(-ball.getYDir())

    if getSpriteCollision(ball, testPlayer):
        ball.setYDir(-ball.getYDir())
        ball.setY(ball.getY()-1)
    # getSpriteCollision(testPlayer, ball)
    # if getSpriteCollision(ball, brick):
    #     ball.setYDir(-ball.getYDir())
    #     brick.setPos(-100, -100)

    
    for i in range(len(brickArray)):
        getBrickCollision(ball, brickArray[i])
        screen.blit(brickArray[i].getBox(), brickArray[i].getPos())


    # screen.blit(testBox.getBox(), testBox.getPos())
    # screen.blit(brick.getBox(), brick.getPos())
    screen.blit(testPlayer.getBox(), testPlayer.getPos())
    # screen.blit(testPlayer.getBox(), (ball.getX()-testPlayer.getWidth()/2, testPlayer.getY()))
    screen.blit(ball.getBox(), ball.getPos())

    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the surface with changes
pygame.quit()

