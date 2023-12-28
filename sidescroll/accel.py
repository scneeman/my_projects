import pygame, sys, random, math
from pygame.locals import QUIT
from player import Player
from block import Block

pygame.init()
w = 600
h = 400
screen = pygame.display.set_mode((w, h))
screen.fill((255, 255, 255))
pygame.display.set_caption('Hello World!')

# the variables
p = Player(w, h)
blocks = []
for i in range(10):
  blocks.append(Block(w, h, random.randint(0,w), random.randint(0,h)))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # acceleration left & right
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    if abs(p.x_v) < p.max_v:
      p.x_v -= 0.01  
  elif keys[pygame.K_LEFT]:
    if p.x_v < p.max_v:
      p.x_v += 0.01
  else: # decelerate
    if abs(p.x_v) > 0:
      p.x_v -= abs(p.x_v)/p.x_v*0.01 # keeps the sign
    if abs(p.x_v) < 0.02: # avoids drift
      p.x_v = 0
  
  # acceleration up & down
  if keys[pygame.K_UP]:
    if p.y_v < p.max_v:
      p.y_v += 0.01
  elif keys[pygame.K_DOWN]:
    if abs(p.y_v) < p.max_v:
      p.y_v -= 0.01
  else:
    if abs(p.y_v) > 0:
      p.y_v -= abs(p.y_v)/p.y_v*0.01
    if abs(p.y_v) < 0.02:
      p.y_v = 0
  
  # move the blocks
  for block in blocks:
    block.x += p.x_v*block.size
    block.y += p.y_v*block.size




  # draw the player and blocks
  p.draw(screen)
  for block in blocks:
    block.draw(screen)

  # when one block goes off screen
  # create a new one on opposite side
  for block in blocks:
    if block.x > w and not block.spawned_new:
      blocks.append(Block(w, h, x=0, y=random.randint(0,h)))
      block.spawned_new = True
      # print(len(blocks))
    if block.x < 0 and not block.spawned_new:
      blocks.append(Block(w, h, x=w, y=random.randint(0,h)))
      block.spawned_new = True
    if block.y > h and not block.spawned_new:
      blocks.append(Block(w, h, x=random.randint(0,w), y=0))
      block.spawned_new = True
    if block.y < 0 and not block.spawned_new:
      blocks.append(Block(w, h, x=random.randint(0,w), y=h))
      block.spawned_new = True
  
  pygame.time.delay(5)
  pygame.display.update()
  screen.fill((255, 255, 255))