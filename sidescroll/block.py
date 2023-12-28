import pygame, random

class Block:
  def __init__(self, w, h, x, y):
    self.x = x
    self.y = y
    self.size = random.randint(3, 15)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    self.color = (r, g, b)
    self.spawned_new = False
    
  
  def draw(self, screen):
    pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

