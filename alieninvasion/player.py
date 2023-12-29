import pygame, random
from ship import Ship

# the Player class will inherit from Ship
# we'll only need __init__ here
class Player(Ship):
    def __init__(self, x=20, y=20, size=5):
        super().__init__(x, y, size)
        self.color = (255,0,255)
        self.xV = 3
        self.yV = 3
  