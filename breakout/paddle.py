from block import *

class Paddle(Block):
  
  def __init__(self, xp, yp, sizep):
    super().__init__(xp, yp, sizep)
    self.r = 0
    self.g = 0
    self.b = 0
    self.a = 255

  def move(self, key, w):
    if self.x < w - self.size//2:
      if key == pygame.K_RIGHT:
        self.x = self.x + self.size

    if self.x > 0:
      if key == pygame.K_LEFT:
        self.x = self.x - self.size

  def move_mouse(self, mouse_pos):
    self.x = mouse_pos[0]
    
    