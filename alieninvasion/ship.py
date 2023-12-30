import pygame, random

# the super class
# we'll need __init__, draw, move
class Ship:
  
    def __init__(self, x=20, y=20, size=5):
        self.x = x
        self.y = y
        self.size = size
        self.xV = random.randint(-5,5)
        self.yV = random.randint(-5,5)
        self.color = (0,0,0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    
    def move(self, screen):
        w, h = screen.get_size()
        if self.x-self.size<0 or self.x+self.size>w:
            self.xV *= -1
        if self.y-self.size<0 or self.y+self.size>h:
            self.yV *= -1
        self.x += self.xV
        self.y += self.yV
    
    


  