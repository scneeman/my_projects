import pygame, random, math

class Bouncy:
  def __init__(self, w, h):
    self.x = random.randint(0,w)
    self.y = random.randint(0,h)
    self.size = random.randint(10, 30)
    self.xv = random.randint(-5,5)
    self.yv = random.randint(-5,5)
    self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

  def move(self):
    w, h = pygame.display.get_surface().get_size()
    if self.x < 0 or self.x > w:
      self.xv *= -1
    if self.y < 0 or self.y > h:
      self.yv *= -1
    self.x += self.xv
    self.y += self.yv


  def was_hit(self, mouse):
    # dist = math.sqrt((mouse[0]-self.x)**2 + (mouse[1]-self.y)**2)
    # return dist <= self.size
    if mouse[0] < self.x+self.size and mouse[0] > self.x - self.size:
      if mouse[1] < self.y+self.size and mouse[1] > self.y - self.size:
        return True
    return False