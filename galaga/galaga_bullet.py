import pygame, random

class bullet:
    def __init__(self, direction, w, x_param, y_param):
        self.x = x_param
        self.y = y_param
        if direction == "up": # for the player
            self.height = int(w/100) + 1
            self.yV = -4
            self.color = (0,255,0)
            self.thickness = int(self.height/2)
        else: # for the enemies
            self.yV = 3
            self.height = int(w/120) + 1
            self.color = (255,0,0)
            self.thickness = int(self.height/2)

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y+self.height), self.thickness)

    def move(self):
        self.y = self.y + self.yV
        
        
