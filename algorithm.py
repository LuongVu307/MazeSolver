import pygame
import sys
from algorithm import Cell, RanDFS, RanPrims, Eller, HuntKill, BinaryTree, RanKruskal

pygame.init()

GUI_WIDTH, GUI_HEIGHT = 800, 500
WIDTH, HEIGHT = 402, 302
TILE = 10
rows, cols = HEIGHT // TILE, WIDTH // TILE

FPS = 60

screen = pygame.display.set_mode((GUI_WIDTH, GUI_HEIGHT))
pygame.display.set_caption("Maze Generator")

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GRAY = (50, 50, 50)

clock = pygame.time.Clock()


def draw_menu(page):

  screen.fill(WHITE)

  button = pygame.Rect(0, 0, 20, 20)
  if page == 1:
    button.center = (GUI_WIDTH - 30, GUI_HEIGHT // 2)
  elif page == 2:
    button.center = (30, GUI_HEIGHT // 2)
  pygame.draw.rect(screen, pygame.Color("black"), button)

  font = pygame.font.Font(None, 36)
  title_text = font.render("Select Maze Generation Algorithm", True, BLACK)
  screen.blit(title_text, (GUI_WIDTH // 2 - title_text.get_width() // 2, 50))

  option1 = ["DFS Maze", "Kruskal's Maze", "Prims Maze"]
  option2 = ["Eller Maze", "HuntKill Maze", "Binary Tree Maze"]
  option_width = 150

  options = option1 if page == 1 else option2

  for option in options:
    option_text = font.render(option, True, BLACK)
    text_rect = option_text.get_rect(center=(option_width, GUI_HEIGHT // 2))
    choice = pygame.Rect(0, 0, 150, 150)
    choice.center = (option_width, GUI_HEIGHT // 2 + 100)
    pygame.draw.rect(screen, pygame.Color("black"), choice)
    screen.blit(option_text, text_rect)
    option_width += 250

  pygame.display.flip()


def draw_text(screen, text, font, color, position):
  text_surface = font.render(text, True, color)
  text_rect = text_surface.get_rect()
  text_rect.left = position[1]
  text_rect.centery = position[0]
  screen.blit(text_surface, text_rect)


def create_button(screen, rect, text, font, normal_color, hover_color,
                  text_color):
  button_hovered = rect.collidepoint(pygame.mouse.get_pos())
  pygame.draw.rect(screen, hover_color if button_hovered else normal_color,
                   rect)
  text_surface = font.render(text, True, text_color)
  text_rect = text_surface.getrect()
  screen.blit(text_surface, text_rect)

  if button_hovered and pygame.mouse.get_pressed()[0]:
    return True

  return False


def main():
  running = True
  state = "menu"
  page = 1
  maze_type = None
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          x, y = pygame.mouse.get_pos()
          if state == "menu":
            if page == 1:
              if 760 <= x <= 780 and 240 <= y <= 260:
                page = 2
              elif 75 <= x <= 225 and 275 <= y <= 425:
                state = "prepare"
                maze_type = "DFS"
              elif 325 <= x <= 475 and 275 <= y <= 425:
                state = "prepare"
                maze_type = "Kruskal"
              elif 575 <= x <= 725 and 275 <= y <= 425:
                state = "prepare"
                maze_type = "Prims"
            elif page == 2:
              if 20 <= x <= 40 and 240 <= y <= 260:
                page = 1
              elif 75 <= x <= 225 and 275 <= y <= 425:
                state = "prepare"
                maze_type = "Eller"
              elif 325 <= x <= 475 and 275 <= y <= 425:
                state = "prepare"
                maze_type = "HuntKill"
              elif 575 <= x <= 725 and 275 <= y <= 425:
                state = "prepare"
                maze_type = "Binary"

    screen.fill(GRAY)

    if state == "menu":
      draw_menu(page)
    elif state == "prepare":
      grid_cell = [
          Cell(col, row, TILE, screen, cols, rows) for row in range(rows)
          for col in range(cols)
      ]

      if maze_type == "DFS":
        current_cell = grid_cell[0]
        stack = []
      elif maze_type == "Kruskal":
        current_cell = grid_cell[0]
        set_cell = [set([i]) for i in range(len(grid_cell))]
      elif maze_type == "Prims":
        current_cell = grid_cell[rows * cols // 2 + cols // 2]
        current_cell.visited = True

      elif maze_type == "Eller":
        current_cell = grid_cell[0]
        count = 0
        set_cell = []
      elif maze_type == "HuntKill":
        current_cell = grid_cell[0]
      elif maze_type == "Binary":
        current_cell = grid_cell[0]
      state = "maze"
      start_time = pygame.time.get_ticks()
      steps = 0
    elif state == "maze":
      steps += 1
      [cells.draw() for cells in grid_cell]
      draw_text(screen,
                f"TIME: {(pygame.time.get_ticks() - start_time) / 1000}",
                pygame.font.Font(None, 24), pygame.Color("Red"), (40, 30))
      draw_text(screen, f"STEPS: {steps}", pygame.font.Font(None, 24),
                pygame.Color("Red"), (70, 30))
      if maze_type == "DFS":
        current_cell, stack = RanDFS(current_cell, stack, grid_cell)
        if not stack:
          state = "end maze"
      elif maze_type == "Kruskal":
        set_cell = RanKruskal(grid_cell, list(set_cell))
        print(set_cell)
        if not set_cell:
          state = "end maze"
      elif maze_type == "Prims":
        if RanPrims(list(grid_cell)):
          grid_cell = RanPrims(list(grid_cell))
        else:
          print("No Path")
          state = "end maze"
      elif maze_type == "Eller":
        set_cell = Eller(grid_cell, rows, cols, count, set_cell)
        count += 1
        if not set_cell:
          state = "end maze"
      elif maze_type == "HuntKill":
        current_cell = HuntKill(current_cell, grid_cell)
        if current_cell == False:
          maze_type = "end maze"
      elif state == "Binary":
        current_cell = BinaryTree(current_cell, grid_cell, cols)
    elif state == "end maze":
      pass

    pygame.display.flip()

    clock.tick(FPS)


if __name__ == "__main__":
  main()
