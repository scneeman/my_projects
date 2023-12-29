import pygame, random
import functions as f

# setup
pygame.init()
w = 400
h = 400
screen = pygame.display.set_mode([w, h])
screen.fill((255, 255, 255))

num_cells = 50
f.draw_lines(screen, num_cells)
pygame.display.flip()

click = False # for mouse drag

# stay on screen
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      f.fill_spot(screen, pos, num_cells)
      click = True
    if event.type == pygame.MOUSEBUTTONUP:
      click = False
    if event.type == pygame.MOUSEMOTION and click: # for dragging mouse
      pos = pygame.mouse.get_pos()
      f.fill_spot(screen, pos, num_cells) 

  f.draw_lines(screen, num_cells)
  pygame.display.flip()

pygame.quit()