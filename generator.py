import pygame
import random
import sys
import os

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


class Cell:

  def __init__(self, x, y):
    self.visited = False
    self.x, self.y = x, y
    self.walls = {"right": True, "left": True, "top": True, "bottom": True}

  def draw(self):
    x, y = self.x * TILE, TILE * self.y

    if self.visited:
      pygame.draw.rect(screen, pygame.Color("black"), (x, y, TILE, TILE))

    if self.walls["right"]:
      pygame.draw.line(screen, pygame.Color("darkorange"), (x + TILE, y),
                       (x + TILE, y + TILE), 1)
    if self.walls["left"]:
      pygame.draw.line(screen, pygame.Color("darkorange"), (x, y + TILE),
                       (x, y), 1)
    if self.walls["top"]:
      pygame.draw.line(screen, pygame.Color("darkorange"), (x, y),
                       (x + TILE, y), 1)
    if self.walls["bottom"]:
      pygame.draw.line(screen, pygame.Color("darkorange"),
                       (x + TILE, y + TILE), (x, y + TILE), 1)

  def draw_current(self):
    x, y = self.x * TILE, TILE * self.y

    pygame.draw.rect(screen, pygame.Color("brown"), (x, y, TILE, TILE))

  def check_cell(self, x, y):
    find_index = lambda x, y: x + y * cols

    if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
      return False

    return grid_cell[find_index(x, y)]

  def check_neighbor(self):
    neighbor = []
    top = self.check_cell(self.x, self.y - 1)
    right = self.check_cell(self.x + 1, self.y)
    bottom = self.check_cell(self.x, self.y + 1)
    left = self.check_cell(self.x - 1, self.y)

    if top and not top.visited:
      neighbor.append(top)
    if right and not right.visited:
      neighbor.append(right)
    if bottom and not bottom.visited:
      neighbor.append(bottom)
    if left and not left.visited:
      neighbor.append(left)

    return random.choice(neighbor) if neighbor else False


def rm_walls(current, next):
  dx = current.x - next.x
  if dx == 1:
    current.walls["left"] = False
    next.walls["right"] = False
  elif dx == -1:
    current.walls["right"] = False
    next.walls["left"] = False

  dy = current.y - next.y

  if dy == 1:
    current.walls["top"] = False
    next.walls["bottom"] = False
  elif dy == -1:
    current.walls["bottom"] = False
    next.walls["top"] = False


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
  current_cell.visited = True
  current_cell.draw_current()

  next_cell = current_cell.check_neighbor()
  if next_cell:
    next_cell.visited = True
    stack.append(current_cell)
    rm_walls(current_cell, next_cell)
    current_cell = next_cell
  elif stack:
    current_cell = stack.pop()
  else:
    sys.exit()

  pygame.display.flip()
  clock.tick(FPS)
