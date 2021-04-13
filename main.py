import sys
import pygame

from cell import Cell
from cell import generate_cells

pygame.init()

WIDTH = 800
HEIGHT = 800

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('El juego de la vida.')

sprites = pygame.sprite.Group()
sprites.add(generate_cells(WIDTH, HEIGHT, 50, 50))

while True:
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()
       
    sprites.draw(surface)

    pygame.display.flip()
    pygame.display.update()