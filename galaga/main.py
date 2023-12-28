# need to make enemies move

from galaga_ship import ship
from galaga_bullet import bullet
from galaga_enemy import enemy

import random, pygame

pygame.init()
# Set up the drawing window
w = 500
h = 400
screen = pygame.display.set_mode([w, h])
pygame.display.set_caption('Galaga')

player = ship(w, h) # the player, width is 1/10 the size of the screen
shots = [] # the players bullets
targets = [] # each is 1/20 the size of the screen
num_targets = 10

'''
# a grid
# first row
for i in range(int(num_targets/2)):
    xpos = (i+1)*int(w/8) + i*int(w/20)
    ypos = int(h/8)
    targets.append(enemy(w, xpos, ypos))
# second row
for i in range(int(num_targets/2)):
    xpos = (i+1)*int(w/8) + i*int(w/20)
    ypos = 2*int(h/8) + int(w/20)
    targets.append(enemy(w, xpos, ypos))
'''

# text
my_font = pygame.font.Font('freesansbold.ttf', 12)
score = 0
text = my_font.render('Score: ' + str(score), True, (0,0,0))
ticker = 0

# Run until the user clicks to close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            # this returns a list [x,y]
            mouse_position = pygame.mouse.get_pos()
            # move paddle
            player.move(mouse_position[0], w)
        # shoot with mouse click or space bar
        if event.type == pygame.MOUSEBUTTONUP:
            #pos = pygame.mouse.get_pos()
            score = score - 1
            shots.append(bullet("up", w, player.x, player.y))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shots.append(bullet("up", w, player.x, player.y))
                score = score - 1
    
    # Fill the background with white, draw stuff
    screen.fill((255, 255, 255))
    player.draw(screen)
    for target in targets:
        target.draw(screen)
    for shot in shots:
        shot.draw(screen)

    # text
    text = my_font.render('Score: ' + str(score), True, (0,0,0))
    screen.blit(text, (0,0))

    pygame.display.flip() # move from display to screen
    pygame.time.delay(10) # slow it down a bit

    # check if bullet hit an enemy
    for shot in shots:
        for target in targets:
            if shot.x >= target.x and shot.x <= target.x + target.size:
                if shot.y >= target.y and shot.y <= target.y+target.size:
                    score = score + 5*(abs(target.yV) + abs(target.xV))
                    shots.remove(shot)
                    targets.remove(target)
    
    # check if enemy hits player
    for target in targets:
        if player.x - player.width/2 < target.x + target.size and player.x + player.width/2 > target.x:
            if player.y < target.y + target.size and player.y + player.height > target.y:
                score = score - 10
                pygame.time.delay(50)
                targets.remove(target)
                targets.append(enemy(w, random.randint(0, int(w-w/20)), random.randint(0, int(h/20))))

    # move
    for shot in shots:
        shot.move()

    for target in targets:
        target.move(w, h)

    # creating a new target
    ticker = ticker + 1
    if ticker%200 == 0 and len(targets)<num_targets:
        targets.append(enemy(w, random.randint(0, int(w-w/20)), random.randint(0, int(h/20))))

# Done! Time to quit.
pygame.time.delay(1000)
pygame.quit()

