import pygame, sys
from pygame.locals import QUIT
from bouncy import Bouncy

pygame.init()
w = 400
h = 400
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')

shapes = []
for i in range(10):
  shapes.append(Bouncy(w, h))


while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # better this way
  if pygame.mouse.get_pressed()[0]:
    for shape in shapes:
      if shape.was_hit(pygame.mouse.get_pos()):
        shapes.remove(shape)
  
  pygame.time.delay(30)
  screen.fill((255, 255, 255))

  # better to move then draw (more consistent mouse clicks)
  for shape in shapes:
    shape.move()
    shape.draw(screen)

  pygame.display.update()
  