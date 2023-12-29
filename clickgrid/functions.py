import pygame, math

def draw_lines(screen, num_cells):
  w,h = screen.get_size()
  cell_size = w/num_cells
  for i in range(1,num_cells):
    pygame.draw.line(screen, (0,0,0), (i*cell_size, 0), (i*cell_size, h))
    pygame.draw.line(screen, (0,0,0), (0,i*cell_size), (w, i*cell_size))
  pygame.display.flip()

def fill_spot(screen, pos, num_cells):
  w,h = screen.get_size()
  cell_size = w/num_cells
  # top left corner
  x = math.floor(pos[0]/cell_size)*cell_size
  y = math.floor(pos[1]/cell_size)*cell_size
  #print(x, y)
  pygame.draw.rect(screen, (255,0,0), (x, y, cell_size, cell_size))
  pygame.display.flip()