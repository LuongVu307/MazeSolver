import pygame
import random


class Cell:

  def __init__(self, x, y, TILE, screen, cols, rows):
    self.TILE = TILE
    self.screen = screen
    self.cols = cols
    self.rows = rows
    self.visited = False
    self.x, self.y = x, y
    self.walls = {"right": True, "left": True, "top": True, "bottom": True}

  def draw(self):
    x, y = self.x * self.TILE, self.TILE * self.y

    if self.visited:
      pygame.draw.rect(self.screen, pygame.Color("black"), (x, y, self.TILE, self.TILE))

    if self.walls["right"]:
      pygame.draw.line(self.screen, pygame.Color("darkorange"), (x + self.TILE, y),
                       (x + self.TILE, y + self.TILE), 1)
    if self.walls["left"]:
      pygame.draw.line(self.screen, pygame.Color("darkorange"), (x, y + self.TILE),
                       (x, y), 1)
    if self.walls["top"]:
      pygame.draw.line(self.screen, pygame.Color("darkorange"), (x, y),
                       (x + self.TILE, y), 1)
    if self.walls["bottom"]:
      pygame.draw.line(self.screen, pygame.Color("darkorange"),
                       (x + self.TILE, y + self.TILE), (x, y + self.TILE), 1)

  def draw_current(self):
    x, y = self.x * self.TILE, self.TILE * self.y

    pygame.draw.rect(self.screen, pygame.Color("brown"), (x, y, self.TILE, self.TILE))

  def check_cell(self, x, y, grid_cell):
    find_index = lambda x, y: x + y * self.cols

    if x < 0 or x > self.cols - 1 or y < 0 or y > self.rows - 1:
      return False

    return grid_cell[find_index(x, y)]

  def check_neighbor(self, grid_cell):
    neighbor = []
    top = self.check_cell(self.x, self.y - 1, grid_cell)
    right = self.check_cell(self.x + 1, self.y, grid_cell)
    bottom = self.check_cell(self.x, self.y + 1, grid_cell)
    left = self.check_cell(self.x - 1, self.y, grid_cell)

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




def RanDFS(current_cell, stack, grid_cell):
  current_cell.visited = True
  current_cell.draw_current()

  next_cell = current_cell.check_neighbor(grid_cell)
  if next_cell:
    next_cell.visited = True
    stack.append(current_cell)
    rm_walls(current_cell, next_cell)
    current_cell = next_cell
  elif stack:
    current_cell = stack.pop()

  return current_cell, stack



def RanPrims(grid_cell):
  ls = []

  for cell in grid_cell:
    if cell.visited is True:
      ls.append(cell)

  while True:  
    chosen_cell = random.choice(ls)
    next_cell = chosen_cell.check_neighbor(grid_cell)
    if next_cell and next_cell.visited == False:
      next_cell.visited = True
      rm_walls(chosen_cell, next_cell)
      next_cell.draw_current()
      break


def Eller(grid_cell, rows, cols, count, set_cell):
  if cols*count < len(grid_cell):

    i = cols*count
    ls = []
    while i < cols*(count + 1) - 1:
      cells = set()
      if random.randint(1, 10) > 5:
        rm_walls(grid_cell[i], grid_cell[i + 1])
        cells.add(i)
        cells.add(i+1)
      else:
       cells.add(i)

      if count > 0:
        if random.randrange(1, 10) > 5:
          rm_walls(grid_cell[i], grid_cell[i - cols])
          cells.add(i)
          cells.add(i - cols)
        else:
          cells.add(i)

      ls.append(cells)
      i += 1
    num = 0
    for i in ls:
      for j in i:
        num += 1
    if num != cols*(count + 1):
      ls.append(set([cols*(count + 1) - 1]))

    merged_sets = []

    for set1 in set_cell:
      merged = False

      for merged_set in merged_sets:
          if any(element in merged_set for element in set1):
              merged_set.update(set1)
              merged = True
              break

      if not merged:
          merged_sets.append(set1.copy())

    for set2 in ls:
      merged = False

      for merged_set in merged_sets:
          if any(element in merged_set for element in set2):
              merged_set.update(set2)
              merged = True
              break

      if not merged:
          merged_sets.append(set2.copy())

    return merged_sets

  else:
    ls = set_cell.copy()
    while True:
      num_set = random.randint(0, len(ls) - 1)
      set_chosen = ls[num_set]

      num_chosen = random.choice(list(set_chosen))
      cell_chosen = grid_cell[num_chosen]

      next_cell = cell_chosen.check_neighbor(grid_cell)
      if next_cell and grid_cell.index(next_cell) not in set_chosen:
        rm_walls(cell_chosen, next_cell)
        next_cell.draw_current()
        set_chosen.add(grid_cell.index(next_cell))
        break

    merged_sets = []

    for new_set in ls:
        sets_to_merge = []

        for existing_set in merged_sets:
            if any(element in existing_set for element in new_set):
                sets_to_merge.append(existing_set)

        if sets_to_merge:
            merged_set = set().union(new_set, *sets_to_merge)
            merged_sets = [s for s in merged_sets if s not in sets_to_merge]
            merged_sets.append(merged_set)
        else:
            merged_sets.append(new_set.copy())

    return merged_sets


def HuntKill(current_cell, grid_cell):
  current_cell.visited = True

  current_cell.draw_current()

  next_cell = current_cell.check_neighbor(grid_cell)
  if next_cell:
    next_cell.visited = True
    rm_walls(current_cell, next_cell)
    current_cell = next_cell
  else:
    for i in range(len(grid_cell)):
      #grid_cell[i].draw_current()
      if grid_cell[i].visited is True:
        if grid_cell[i].check_neighbor(grid_cell):
          current_cell = grid_cell[i]
          break

  return current_cell


def BinaryTree(current_cell, grid_cell, cols):
  current_cell.visited = True
  if random.randint(1, 10) > 3:
    current_cell.walls["left"] = False
  if random.randint(1, 10) > 3:
    if grid_cell.index(current_cell) > cols:
      current_cell.walls["top"] = False
  current_cell.draw_current()
  if grid_cell.index(current_cell) < len(grid_cell) - 1:
    current_cell = grid_cell[grid_cell.index(current_cell) + 1]
  return current_cell


def RanKruskal(grid_cell, set_cell):
  while True:
    choice = random.randint(0, len(grid_cell)-1)
    current_cell = grid_cell[choice]
    next_cell = current_cell.check_neighbor(grid_cell)
    next_choice = grid_cell.index(next_cell)
    first, second = None, None
    if next_cell:
      for i in range(len(set_cell)):
        if choice in set_cell[i]:
          first = i
        if next_choice in set_cell[i]:
          second = i

    if first != second:
      print(first, second)
      #print(set_cell[first], set_cell[second], "NEW")
      new_cell = set_cell[first] | set_cell[second]
      #print("NEW", new_cell)
      set_cell[first] = new_cell
      set_cell.pop(second)
      rm_walls(current_cell, next_cell)
      break

  print(set_cell)
  return set_cell
          
            
