import pygame, random
import functions as f

# 0 = open spot
# 999 = blocked spot
# 9999 = start
# 1 = goal
# 998 = visited

# setup
pygame.init()
w = 400
h = 400
screen = pygame.display.set_mode([w, h])

# the variables and such
size = 10 # the size of the 2D list, assume a square
grid = f.randomize(size) # randomize the grid, a 2D list

# these can be variable
start_row = 1
start_col = 2
end_row = 8
end_col = 8

# must use these values
grid[start_row][start_col] = 9999
grid[end_row][end_col] = 1

print(grid) # for debugging

f.draw_screen(screen, grid, 'initial screen')

# the magic
grid = f.perform_wave(screen, grid) # this calculates the best path
pygame.time.delay(3000)
# temp = input("\n...press any key...")
grid = f.navigate(screen, grid, start_row, start_col) # this navigates the path
print('done')

