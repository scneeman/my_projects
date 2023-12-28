import pygame, random

class Block:
  def __init__(self, xp, yp, sizep):
    self.x = xp
    self.y = yp
    self.size = sizep
    self.r = random.randint(0,255)
    self.g = random.randint(0,255)
    self.b = random.randint(0,255)
    self.a = random.randint(0,255)
    

  def draw(self, screen):
    pygame.draw.rect(screen,  (self.r, self.g, self.b, self.a),  (self.x, self.y, self.size, self.size//5)  )
                     
    
  