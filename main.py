import sys
import pygame

from cell import Cell
from cell import generate_cells

from ant import Ant

pygame.init()

WIDTH = 1200
HEIGHT = 1000

WIDTH_CELL = 30
HEIGHT_CELL = 30

START = False

FPS = 30
REFRESH_PER_SECONDS = 1000

fps_clock = pygame.time.Clock()

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('La hormiga de Langton.')

current_second = 0

sprites = pygame.sprite.Group()

cells = generate_cells(WIDTH, HEIGHT, WIDTH_CELL, HEIGHT_CELL)

ant = Ant(len(cells)//2, len(cells[0])// 2)
ant.check(cells)

sprites.add(cells)
           
while True:
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            START = True
    
    if START:
        second = time // REFRESH_PER_SECONDS

        if second != current_second:
            ant.check(cells)

            current_second = second

    sprites.draw(surface)

    pygame.display.flip()
    pygame.display.update()

    fps_clock.tick(FPS)