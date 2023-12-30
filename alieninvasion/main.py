import pygame, sys
from pygame.locals import QUIT


# setup pygame surface
pygame.init()
w = 400
h = 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')


# the first screen
# print a welcome message
# wait for click
clicked = False
while not clicked:
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
    
    screen.fill((255,255,255))
    my_font = pygame.font.Font('freesansbold.ttf', 12)
    
    my_text = my_font.render("welcome to my game!", True, (0,0,0))
    screen.blit(my_text, (50,50))
    
    my_text = my_font.render("use arrow keys and mouse", True, (0,0,0))
    screen.blit(my_text, (50, 100))
    pygame.display.update()
    


# setup the 'Player'
# place the player near the bottom center
from player import Player
p = Player(w//2, round(h*0.8), 8)

# setup the list of 'Bullet' objects
from bullet import Bullet
bullets = []

# setup the list of 'Enemy' objects
# the enemies should spawn from near the top middle
from enemy import Enemy
enemies = []
for i in range(10):
    temp = Enemy(x=w//2, y=0.1*h)
    enemies.append(temp)



# the animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # mouse clicks will shoot a bullet
        if event.type == pygame.MOUSEBUTTONDOWN:
            temp = Bullet(p.x, p.y, h//50)
            bullets.append(temp)

    # draw the new screen
    screen.fill((255,255,255))
    
    # arrow keys for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and p.x < w:
        p.x += p.xV
    if keys[pygame.K_LEFT] and p.x > 0:
        p.x -= p.xV
    if keys[pygame.K_UP] and p.y > h//2:
        p.y -= p.yV
    if keys[pygame.K_DOWN] and p.y < h:
        p.y += p.yV

    
    # draw the player
    p.draw(screen)
    
    # draw the bullets (if it is onscreen)
    # remove bullets that have moved offscreen
    for b in bullets:
        if b.y > 0:
            b.draw(screen)
            b.move()
        else:
            bullets.remove(b)
    
    # draw the enemies
    for e in enemies:
        e.draw(screen)
        e.move(screen)
    
    # the magic for collision
    # for each bullet, check if it hit an enemy
    for b in bullets:
        if b.check_hit(enemies):
            bullets.remove(b)
    
    # update the screen and pause
    pygame.display.update()
    pygame.time.delay(20)
    
    # end game check
    if len(enemies) == 0:
        running = False
    
    

    
# after gameplay is over
# clear the screen and display a message
screen.fill((255,255,255))
my_font = pygame.font.Font("freesansbold.ttf", 12)
my_text = my_font.render("Nice job!", True, (0,0,0))
screen.blit(my_text, (50,50))
pygame.display.update()