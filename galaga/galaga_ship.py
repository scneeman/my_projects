import pygame, random
from galaga_bullet import bullet

class ship:

    def __init__(self, w, h):
        self.width = int(w/10)
        self.height = int(self.width)
        self.x = int(w/2)
        self.y = int(8*h/10)

    def draw(self, screen):
        pygame.draw.polygon(screen, (0,0,255), [(self.x, self.y), (self.x+self.width/2, self.y+self.height), (self.x-self.width/2, self.y+self.height)])

    def move(self, param, w):
        # if mouse is off the screen
        if param < 0:
            param = 0
        elif param > w:
            param = w
        self.x = param
        # keep the paddle on the screen
      

