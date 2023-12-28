import pygame, random

class enemy:
    def __init__(self, w, x_param, y_param):
        self.x = x_param
        self.y = y_param
        self.size = int(w/20)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.back_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.yV = random.randint(1, 2)
        self.xV = 0
        while self.xV == 0:
            self.xV = random.randint(-2, 2)
        self.tick = 0
        self.max_tick = random.randint(40, 80)

    def draw(self, screen):
        pygame.draw.rect(screen, self.back_color, (self.x+int(self.size/8), self.y+int(self.size/8), self.size, self.size))        
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def move(self, w, h):
        # switch between left/right, bounce on wall
        self.tick = self.tick + 1
        if self.tick >= self.max_tick or self.x + self.size >= w or self.x <= 0:
            self.tick = 0
            self.xV = -1*self.xV
        # move
        self.x = self.x + self.xV
        self.y = self.y + self.yV
        if self.y > h:
            self.y = 0
    