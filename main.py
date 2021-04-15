import sys
import pygame

from cell import Cell
from cell import generate_cells

pygame.init()

WIDTH = 1200
HEIGHT = 800

START = False

FPS = 30
REFRESH_PER_SECONDS = 200

fps_clock = pygame.time.Clock()

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Juego de la vida.')

current_second = 0
sprites = pygame.sprite.Group()

cells = generate_cells(WIDTH, HEIGHT, 40, 40)

sprites.add(cells)

def start_algorithm():
    for row in cells:
        for cell in row:
            neighborhoods = cell.get_neighborhoods(cells)

            if cell.life:
                if not len(neighborhoods) in (2, 3):
                    cell.change()
            else:
                if len(neighborhoods) == 3:
                    cell.change()

    START = False
           
def update_cells():
    for row in cells:
        for cell in row:
            cell.update()

while True:
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_position = pygame.mouse.get_pos()

            for cell in sprites:
                if cell.rect.collidepoint(current_position):
                    cell.select()
                    print(cell.pos_x, cell.pos_y)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            START = True
        
        # Restart Game!
        if pressed[pygame.K_r] and START:
            for row in cells:
                for cell in row:
                    cell.restart()
            
            START = False
        
        # Stop Algoritm
        if pressed[pygame.K_s] and START:
            START = False

    if START:
        second = time // REFRESH_PER_SECONDS

        if second != current_second:
            start_algorithm()
            update_cells()

            current_second = second

    sprites.draw(surface)

    pygame.display.flip()
    pygame.display.update()

    fps_clock.tick(FPS)