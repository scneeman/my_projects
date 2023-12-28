import pygame, sys, random, math
from pygame.locals import QUIT

# the function



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
    
    # TODO mouse (tabbed in events or not?? try both!)
    
    pygame.time.delay(10)
    pygame.display.update()
# ---- end of animation loop
