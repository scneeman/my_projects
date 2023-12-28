import pygame, random

class snek_ball:
    def __init__(self, rad_param=10, x_param=100, y_param=100, dir_param=1, col_param=(250, 250, 250)):
        self.rad = rad_param
        self.x = x_param
        self.y = y_param
        self.dir = dir_param
        self.r = col_param[0]
        self.g = col_param[1]
        self.b = col_param[2]


    def draw(self, screen):
        pygame.draw.circle(screen, (self.r, self.g, self.b), (self.x, self.y), self.rad)

    def move(self):
        w, h = pygame.display.get_surface().get_size()
        if self.x > w or self.x < 0:
            self.dir = 0
        if self.y > h or self.y < 0:
            self.dir = 0

        if self.dir == 1:
            self.y = self.y - 2*self.rad
        elif self.dir == 2:
            self.x = self.x + 2*self.rad
        elif self.dir == 3:
            self.y = self.y + 2*self.rad
        elif self.dir == 4:
            self.x = self.x - 2*self.rad


