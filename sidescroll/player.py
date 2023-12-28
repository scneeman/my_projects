import pygame

class Player:
  def __init__(self, w, h):
    self.x = w//2
    self.y = h//2
    self.size = 15
    self.x_v = 1
    self.y_v = 1
    self.max_v = 0.6


  def draw(self, screen):
    pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.size)