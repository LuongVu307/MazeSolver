import pygame
import random
import sys
import os
from algorithm import Cell, RanDFS, RanPrims, Eller, HuntKill, BinaryTree, RanKruskal

pygame.init()

WIDTH, HEIGHT = 402, 302
TILE = 10
rows, cols = HEIGHT // TILE, WIDTH // TILE

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GRAY = (50, 50, 50)

clock = pygame.time.Clock()

grid_cell = [Cell(col, row, TILE, screen, cols, rows) for row in range(rows) for col in range(cols)]

#current_cell = grid_cell[0]
#stack = []

#current_cell = grid_cell[rows*cols//2 + cols//2]
#current_cell.visited = True

#current_cell = grid_cell[0]
#count = 0
#set_cell = []

#current_cell = grid_cell[0]

current_cell = grid_cell[0]
set_cell = []

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      sys.exit()

  screen.fill(GRAY)

  [cells.draw() for cells in grid_cell]

  #current_cell, stack = RanDFS(current_cell, stack, grid_cell)

  #RanPrims(grid_cell)

  #set_cell = Eller(grid_cell, rows, cols, count, set_cell)
  #count += 1

  #current_cell = HuntKill(current_cell, grid_cell)

  #current_cell = BinaryTree(current_cell, grid_cell, cols)

  set_cell = RanKruskal(grid_cell, set_cell)

  pygame.display.flip()
  clock.tick(FPS)
