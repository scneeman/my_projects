import pygame, random

class snek_square:
    def __init__(self, size_param = 20, x_param = 200, y_param = 200, dir_param = 1, lead_param = False):
        self.is_leader = lead_param
        self.dir = dir_param
        self.col_place = random.randint(0,2)
        self.seed_num = random.randint(1,100)
        self.x = x_param
        self.y = y_param
        self.size = size_param

    def draw(self, screen):
        # a white outline
        pygame.draw.rect(screen, (255,255,255), (self.x-2, self.y-2, self.size+4, self.size+4))
        # each piece is the same random each time
        #random.seed(self.seed_num) # sets all future random seeds
        # coloring the block
        for temp_row in range(4):
            for temp_col in range(4):   
                if self.is_leader:
                    col = (255,0,0)                  
                elif self.col_place == 0:
                    col = (random.randint(100,255), 0, 0)
                elif self.col_place == 1:
                    col = (0, random.randint(100,255), 0)
                else:
                    col = (0, 0, random.randint(100,255))
                pygame.draw.rect(screen, col, (self.x + temp_col*(self.size/4), self.y + temp_row*(self.size/4), self.size/4, self.size/4))


    def move(self):
        w, h = pygame.display.get_surface().get_size()
        if self.x + self.size > w or self.x < 0:
            self.dir = 0
        if self.y + self.size > h or self.y < 0:
            self.dir = 0

        if self.dir == 1:
            self.y = self.y - self.size
        elif self.dir == 2:
            self.x = self.x + self.size
        elif self.dir == 3:
            self.y = self.y + self.size
        elif self.dir == 4:
            self.x = self.x - self.size



