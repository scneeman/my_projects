import pygame, random
from ship import Ship

# an 'Enemy' will inherit from the 'Ship' class
# we'll only need the __init__ method here
class Enemy(Ship):
    def __init__(self, x=20, y=20, size=10):
        super().__init__(x, y, size)
        self.color = (255,0,0)
    