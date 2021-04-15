import sys
import pygame

from cell import Cell
from cell import generate_cells

pygame.init()

WIDTH = 800
HEIGHT = 800

START = False

FPS = 30 # frames per second setting
fps_clock = pygame.time.Clock()

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('El juego de la vida.')

current_second = 0
sprites = pygame.sprite.Group()

cells = generate_cells(WIDTH, HEIGHT, 50, 50)

sprites.add(cells)

"""
Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").
"""

def start_algorithm(cells):
    for row in cells:
        for cell in row:
            neighborhoods = cell.get_neighborhoods(cells)

            if cell.life:
                print(len(neighborhoods))

                if len(neighborhoods) in (2, 3):
                    pass
                else:
                    cell.set_next_life()
            else:
                if len(neighborhoods) == 3:
                    cell.set_next_life()

while True:
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_position = pygame.mouse.get_pos()

            for cell in sprites:
                if cell.rect.collidepoint( current_position ):
                    cell.set_next_life()
                    cell.select()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            START = True
            print('Comenzamos con el algoritmo')

    if START:
        second = time // 1000

        if second != current_second:
            start_algorithm(cells)
            
            sprites.draw(surface)
            current_second = second

        for row in cells:
            for cell in row:
                cell.select()
    else:
        sprites.draw(surface)

    pygame.display.flip()
    pygame.display.update()

    fps_clock.tick(FPS)