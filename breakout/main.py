import pygame, random
from bouncy import *
from block import *
from paddle import *

# setup
w = 400
h = 300
screen = pygame.display.set_mode([w, h])

# TODO create a 'bouncy' object
s = w//40
ball = Bouncy(s)
pad = Paddle(w//2, 0.8*h, w//5)

# TODO create a list of 'block' objects
blocks = []

for i in range(100):
  size = w//20
  x = random.randint(0, w-size)
  y = random.randint(0, h//5)
  blocks.append(Block(x, y, size))
  
# TODO create a 'paddle' object

  
# stay on screen
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    #if event.type == pygame.KEYDOWN:
      #pad.move(event.key, w)
    if event.type == pygame.MOUSEMOTION:
      mouse_pos = pygame.mouse.get_pos()
      pad.move_mouse(mouse_pos)

    
  # fill the background with white (or don't!)
  screen.fill((255, 255, 255))

  # TODO draw and move
  ball.draw(screen)
  ball.move(w, h)

  pad.draw(screen)
  
  for b in blocks:
    b.draw(screen)

  # TODO check for collision
  ball.check_collision(pad)

  for b in blocks:
    if ball.collides_with(b):
      blocks.remove(b)
  

  # pushes the screen to the current display
  pygame.display.flip()

  # delay a moment
  pygame.time.delay(7)


