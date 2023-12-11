import pygame
import random
import sys
import os
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
set_cell = [set([i]) for i in range(len(grid_cell))]

def draw_menu(option="1"):
  
  screen.fill(WHITE)

  button = pygame.Rect(0, 0, 20, 20)
  button.center = (GUI_WIDTH-30, GUI_HEIGHT//2)
  pygame.draw.rect(screen, pygame.Color("black"), button)
  
  font = pygame.font.Font(None, 36)
  title_text = font.render("Select Maze Generation Algorithm", True, BLACK)
  screen.blit(title_text, (GUI_WIDTH // 2 - title_text.get_width() // 2, 50))
  
  option1 = ["DFS Maze", "Kruskal's Maze", "Prims Maze"]
  option2 = ["Eller Maze", "HuntKill Maze", "Binary Tree Maze"]
  option_width = 150
  
  for option in option1:
      option_text = font.render(option, True, BLACK)
      text_rect = option_text.get_rect(center=(option_width, GUI_HEIGHT//2))
      screen.blit(option_text, text_rect)
      option_width += 250
  
  pygame.display.flip()
  
  
  





def main():
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        sys.exit()
  
    screen.fill(GRAY)
    
  
    #current_cell, stack = RanDFS(current_cell, stack, grid_cell)
  
    #RanPrims(grid_cell)
  
    #set_cell = Eller(grid_cell, rows, cols, count, set_cell)
    #count += 1
  
    #current_cell = HuntKill(current_cell, grid_cell)
  
    #current_cell = BinaryTree(current_cell, grid_cell, cols)
    
    #set_cell = RanKruskal(grid_cell, list(set_cell))
    #[cells.draw() for cells in grid_cell]


    draw_menu()
    pygame.display.flip()
  
    clock.tick(FPS)



if __name__ == "__main__":
  main()
