from snek_player import snek_player
from snek_square_player import snek_square_player
from snek_food import snek_food

import pygame, math

# Set up the drawing window
pygame.init()
w = 500
h = 400
screen = pygame.display.set_mode([w, h])

# text
score = 0
my_font = pygame.font.Font('freesansbold.ttf', 12)
text = my_font.render('Score: ' + str(score), True, (0,0,0))
max_time = 40
timer = max_time
my_font2 = pygame.font.Font('freesansbold.ttf', 24)
text2 = my_font2.render('Timer: ' + str(timer), True, (0,0,0))


# two versions of the player
# also must change the 'hit' check
#player = snek_player(5) # constructing the initial player
player = snek_square_player(5)

delay = 250
temp_dir = 1 # default direction is up

# bunch of food
foods = []
for i in range(10):
    foods.append(snek_food(screen))


# Run until the user clicks to close
running = True
while running: 

    # looking for input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # don't allow reverse direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if temp_dir != 3:
                    temp_dir = 1
            if event.key == pygame.K_DOWN:
                if temp_dir != 1:
                    temp_dir = 3
            if event.key == pygame.K_LEFT:
                if temp_dir != 2:
                    temp_dir = 4
            if event.key == pygame.K_RIGHT:
                if temp_dir != 4:
                    temp_dir = 2
            player.change_dir(temp_dir)
    
    # erase the previous, draw new
    screen.fill((0, 255, 255)) 
    for item in foods:
        item.draw(screen)
    player.draw_player(screen)

    # text
    text = my_font.render('Score: ' + str(score), True, (0,0,0))
    screen.blit(text, (0,0))
    text2 = my_font2.render('Time: ' + str(timer), True, (0,0,0))
    screen.blit(text2, (0,60))

    # necessary stuff
    pygame.display.flip() # move from display to screen
    pygame.time.delay(delay) # slow it down a bit

    # check for eating food
    hit = False
    place = 0
    for i in range(len(foods)):
        dist = math.sqrt((foods[i].x - player.pieces[0].x)**2 + (foods[i].y - player.pieces[0].y)**2)
        # if distance is small, delete food, add segment
        #if dist < 2*player.rad: # for ball version
        if dist < player.size:
            hit = True
            place = i        
            break

    if hit:
        player.add_piece()
        del foods[place]
        foods.append(snek_food(screen))
        timer = max_time



    # move
    player.move_player()
    # if hit an edge, game over
    if player.pieces[0].dir == 0:
        running = False

    # fun experiment
    score = score + 1
    #if score % 5 == 0:
    #    player.add_piece()
    if score % 10 == 0:
        if delay > 100:
                delay = delay - int(0.02*delay)
        
    if timer <= 0:
        running = False
    timer = timer - 1


# Done! Time to quit.
pygame.time.delay(1000)
pygame.quit()