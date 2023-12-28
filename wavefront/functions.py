import pygame, random, math

stall = 500

# randomize the grid
def randomize(size):
  mat = [[0]*size for _ in range(size)]
  for i in range(len(mat)):
    for j in range(len(mat)):
      num = random.randint(0,9)
      if num < 8: # about 80% will be 'open'
        mat[i][j] = 0
      else:
        mat[i][j] = 999
  return mat

# draws the grid lines
def draw_lines(screen, num_cells):
  w,h = screen.get_size()
  cell_size = w/num_cells
  for i in range(1,num_cells):
    pygame.draw.line(screen, (200,200,200), (i*cell_size, 0), (i*cell_size, h))
    pygame.draw.line(screen, (200,200,200), (0,i*cell_size), (w, i*cell_size))

# draws the graphics version of the grid
# note the use of y and x for rows and columns
def draw_grid(screen, mat, text=-99):
  num_cells = len(mat)
  w,h = screen.get_size()
  cell_size = w/num_cells
  my_font = pygame.font.Font('freesansbold.ttf', 12)
  if text != -99:
    text = my_font.render(text, True, (0,0,0))
    screen.blit(text, (0,0))
  for y in range(len(mat)):
    for x in range(len(mat[0])):
      if mat[y][x]==999: # blocked
        pygame.draw.line(screen, (255,0,0), (x*cell_size, y*cell_size), ((x+1)*cell_size, (y+1)*cell_size))
        pygame.draw.line(screen, (255,0,0), (x*cell_size, (y+1)*cell_size), ((x+1)*cell_size, y*cell_size))
      elif mat[y][x]==9999: # current position
        pygame.draw.circle(screen, (0,255,0), (x*cell_size+cell_size/2, y*cell_size + cell_size/2), cell_size/2)
      elif mat[y][x]==1: # goal
        pygame.draw.rect(screen, (0,255,0), (x*cell_size, y*cell_size, cell_size, cell_size))
        text = my_font.render('goal', True, (0,0,0))
        screen.blit(text, (x*cell_size + cell_size/10,y*cell_size+cell_size/2))
      elif mat[y][x]==998: # visited
        pygame.draw.circle(screen, (0,0,255), (x*cell_size+cell_size/2, y*cell_size + cell_size/2), cell_size/2)     
      else: # otherwise
        if mat[y][x] == 0:
          temp = ''
        else:
          temp = str(mat[y][x])
        text = my_font.render(temp, True, (0,0,0))
        screen.blit(text, (x*cell_size + cell_size/10,y*cell_size+cell_size/2))

def draw_screen(screen, mat, text=-99):
  screen.fill((255, 255, 255))
  num_cells = len(mat)
  draw_lines(screen, num_cells)
  draw_grid(screen, mat, text)
  pygame.display.flip()
  pygame.time.delay(stall)
        
# begins at the goal, marks up any adjacent cells that are open
def perform_wave(screen, mat): 
  global stall
  cur_wave = 1
  found_goal = False
  size = len(mat)
  while cur_wave < size*size and not found_goal:
    mat, found_goal = one_wave(mat, cur_wave) # calls the function below
    draw_screen(screen, mat, 'current wave: ' + str(cur_wave))
    cur_wave = cur_wave + 1 
  #print(mat) # for debugging
  return mat

# checks NSEW for done, then checks for open spot, marks up by 1 
# note that this begins at the 'end', marking adjacent cells up
def one_wave(mat, cur_wave):
  done = False
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j]==cur_wave:
        if i > 0: # check north
          if mat[i-1][j]==9999:
            done = True
          elif mat[i-1][j]==0:
            mat[i-1][j] = cur_wave + 1        
        if i < len(mat)-1: # check south
          if mat[i+1][j]==9999:
            done = True
          elif mat[i+1][j]==0:
            mat[i+1][j] = cur_wave + 1       
        if j < len(mat[0])-1: # check east
          if mat[i][j+1]==9999:
            done = True 
          elif mat[i][j+1]==0:
            mat[i][j+1] = cur_wave + 1       
        if j > 0: # check west
          if mat[i][j-1]==9999:
            done = True
          elif mat[i][j-1] == 0:
            mat[i][j-1] = cur_wave + 1
  return mat, done

# checks in adjacent cells for smallest number
# then 'moves' there
def navigate(screen, mat, cur_row, cur_col):
  global stall
  at_goal = False
  size = len(mat)
  
  while not at_goal:
    min = 99999
    dir = 0
    if cur_row > 0: # check north
      if mat[cur_row-1][cur_col] == 1:
        dir = 1
        at_goal = True
        min = mat[cur_row-1][cur_col]
      elif mat[cur_row-1][cur_col] < min and mat[cur_row-1][cur_col] != 0:
        min = mat[cur_row-1][cur_col]
        dir = 1
    if cur_row < len(mat) - 1: # check south
      if mat[cur_row+1][cur_col] == 1:
        dir = 3
        at_goal = True
        min = mat[cur_row+1][cur_col]
      elif mat[cur_row+1][cur_col] < min and mat[cur_row+1][cur_col] != 0:
        min = mat[cur_row+1][cur_col]
        dir = 3       
    if cur_col<len(mat[0])-1: # check east
      if mat[cur_row][cur_col+1] == 1:
        dir = 2
        at_goal = True
        min = mat[cur_row][cur_col+1]
      elif mat[cur_row][cur_col+1] < min and mat[cur_row][cur_col+1] != 0:
        min = mat[cur_row][cur_col+1]
        dir = 2
    if cur_col > 0: # check west
      if mat[cur_row][cur_col-1] == 1:
        dir = 4
        at_goal = True
        min = mat[cur_row][cur_col-1]
      elif mat[cur_row][cur_col-1]<min and mat[cur_row][cur_col-1] != 0:
        min = mat[cur_row][cur_col-1]
        dir = 4
    # update the current position
    mat[cur_row][cur_col] = 998 # mark it visited
    if dir == 1:
      cur_row = cur_row - 1
    elif dir == 2:
      cur_col = cur_col + 1
    elif dir == 3:
      cur_row = cur_row + 1
    else:
      cur_col = cur_col - 1
    mat[cur_row][cur_col] = 9999

    # draw the new screen
    draw_screen(screen, mat, 'navigating the path...')

  