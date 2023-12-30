import pygame

# the Bullet class
# we'll need __init__, draw, move, check_hit
class Bullet:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0,0,0)
        self.yV = -3
    
    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y + self.size))
    
    def move(self):
        self.y += self.yV
    
  # for each enemy in the list
  # check if this bullet hits that enemy (remove that enemy)
    def check_hit(self, enemies):
        for e in enemies:
            if self.x > e.x - e.size and self.x < e.x + e.size:
                if self.y > e.y - e.size and self.y < e.y + e.size:
                    enemies.remove(e)
                    return True
    