import pygame
import random
import sys
import os
from algorithm import Cell, RanDFS

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

grid_cell = [Cell(col, row) for row in range(rows) for col in range(cols)]

current_cell = grid_cell[0]
stack = []

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      sys.exit()

  screen.fill(GRAY)

  [cells.draw() for cells in grid_cell]

  current_cell, stack = RanDFS(current_cell, stack, grid_cell)

  pygame.display.flip()
  clock.tick(FPS)
