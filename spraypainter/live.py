import pygame, sys, random, math
from pygame.locals import QUIT

# the function
# start with square, then improve
def spray(screen, x_cent, y_cent, color):
for i in range(50):
    # x_rand = random.randint(-5,5)
    # y_rand = random.randint(-5,5)
    theta = random.uniform(0, 2*math.pi)
    r = random.uniform(0, random.uniform(5,10))
    x_rand = int(r*math.cos(theta))
    y_rand = int(r*math.sin(theta))
    pos = (x_cent + x_rand, y_cent + y_rand)
    screen.set_at(pos, color) # draws a pixel

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
    # TODO keypress
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            color = (255,0,0)
        if event.key == pygame.K_g:
            color = (0,255,0)
        if event.key == pygame.K_SPACE:
            pass
      
    # TODO mouse (tabbed in events or not?? try both!)
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        spray(screen, x, y, color)
    
    pygame.time.delay(10)
    pygame.display.update()
# ---- end of animation loop
