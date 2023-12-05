import pygame
import random
import sys
import os

try:
    pygame.init()
except pygame.error as e:
    print("Pygame initialization failed:", e)


pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")


BLACK = (0, 0, 0)
WHITE = (250, 250, 250)


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLACK)




    pygame.display.flip()
    clock.tick(FPS)

    


