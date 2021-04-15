import sys
import pygame

from cell import Cell
from cell import generate_cells

pygame.init()

WIDTH = 800
HEIGHT = 800

START = False

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('El juego de la vida.')

current_second = 0
sprites = pygame.sprite.Group()

cells = generate_cells(WIDTH, HEIGHT, 50, 50)

sprites.add(cells)

def start_algorithm(cells):
    for row in cells:
        for cell in row:
            
            neighborhoods = cell.get_neighborhoods(cells)

            if cell.life:
                if len(neighborhoods) == 2 or len(neighborhoods) == 3:
                    pass
                else:
                    cell.select()
            else:
                if len(neighborhoods) == 3:
                    cell.select()

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
    else:
        sprites.draw(surface)

    pygame.display.flip()
    pygame.display.update()
