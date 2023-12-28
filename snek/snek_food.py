import random, pygame

class snek_food:
    def __init__(self, screen):
        w, h = pygame.display.get_surface().get_size()
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)
        self.rand_r = random.randint(0,255)
        self.rand_g = random.randint(0,255)
        self.rand_b = random.randint(0,255)

    def draw(self, screen):
        pygame.draw.rect(screen, (self.rand_r, self.rand_g, self.rand_b), (self.x, self.y, 10, 10))

