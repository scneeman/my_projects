import pygame, sys, random, math
from pygame.locals import QUIT

# the functions
def square(x_cent, y_cent):
    x_rand = random.randint(-5,5)
    y_rand = random.randint(-5,5)
    pos = (x_cent+x_rand, y_cent+y_rand)
    screen.set_at(pos, (0,0,0))
    
def spray(x_cent, y_cent, color):
    # a random distance from center
    # also a random spray radius
    r = random.uniform(0, random.uniform(5,10))
    theta = random.uniform(0, 2*math.pi)
    x_rand = int(r*math.cos(theta))
    y_rand = int(r*math.sin(theta))
    pos = (x_cent+x_rand, y_cent+y_rand)
    screen.set_at(pos, color)


# the setup
pygame.init()
w = 400
h = 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))
color = (0,0,0)


# the animation loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # change color with keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255,0,0)
            if event.key == pygame.K_g:
                color = (0,255,0)
            if event.key == pygame.K_b:
                color = (0,0,255)
            if event.key == pygame.K_SPACE:
                color = (0,0,0)
    
    # this gets the state of the left button
    # this can be tabbed in the events section or not
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        spray(x, y, color)
    
    pygame.display.update()