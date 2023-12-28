import pygame, random

class Bouncy:
  # TODO improvement
  # make the size of the ball depend on the screen size
  def __init__(self, sizep):
    self.x = 100
    self.y = 100
    self.size = sizep
    # never zero velocity!
    self.xV = 0
    while self.xV == 0:
      self.xV = random.randint(-3,3)
    self.yV = 0
    while self.yV == 0:
      self.yV = random.randint(-3,3)
    self.red = random.randint(0,255)
    self.green = random.randint(0,255)
    self.blue = random.randint(0,255)
      

  def draw(self, screen):
    pygame.draw.circle(screen, (self.red, self.green, self.blue), (self.x, self.y), self.size)
  
  def move(self, w, h):
    if self.x < 0 or self.x > w:
      self.xV = -1*self.xV
    if self.y < 0 or self.y > h:
      self.yV = -1*self.yV

    self.x = self.x + self.xV
    self.y = self.y + self.yV

  def check_collision(self, pad):
    # if close in both x & y
    if self.x > pad.x and self.x < pad.x + pad.size:
      if self.y > pad.y:
        self.yV = -1 * self.yV


  def collides_with(self, block):
    if self.x > block.x and self.x < block.x + block.size:
      if self.y > block.y and self.y < block.y + block.size//5:
        self.yV = -1 * self.yV
        return True
    return False