import pygame, sys
from pygame.locals import QUIT
from player import Player
from block import Block
import random

pygame.init()
w = 600
h = 400
screen = pygame.display.set_mode((w, h))
screen.fill((255, 255, 255))
pygame.display.set_caption('Hello World!')


p = Player(w, h)
blocks = []
for i in range(10):
  blocks.append(Block(w, h, random.randint(0,w), random.randint(0,h)))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # get keyboard input
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    p.x_v = -1
  elif keys[pygame.K_LEFT]:
    p.x_v = 1
  else:
    p.x_v = 0
  if keys[pygame.K_UP]:
    p.y_v = 1
  elif keys[pygame.K_DOWN]:
    p.y_v = -1
  else:
    p.y_v = 0
  # move the blocks

  for block in blocks:
    block.x += p.x_v * p.max_v * block.size
    block.y += p.y_v * p.max_v * block.size

  # draw the player and blocks
  p.draw(screen)
  for block in blocks:
    block.draw(screen)

  # when a block goes off screen
  # spawn a new one on the opposite side
  for block in blocks:
    if block.x > w and not block.spawned_new:
      blocks.append(Block(w, h, x=0, y=random.randint(0,h)))
      block.spawned_new = True
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