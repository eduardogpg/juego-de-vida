import sys

import pygame

from celula import Celula

def get_vecinos(pos_x, pos_y, celulas):
    vecinos = list()
        
    for x in range(pos_x - 1, pos_x + 2):
        for y in range(pos_y - 1, pos_y + 2):
            try:
                vecinos.append(celulas[x][y])
            except:
                pass

    return vecinos

pygame.init()

WIDTH = 800
HEIGHT = 1000

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('El juego de la vida.')

sprites = pygame.sprite.Group()

start = False
id = 0
celulas = list()
initial_pos_y = 0

for _ in range(0, 25):
        
    initial_pos_x = 0
    lista_b = list()

    for _ in range(0, 25):

        celula = Celula(
            id=id,
            width=50,
            height=50,
            pos_x=initial_pos_x,
            pos_y=initial_pos_y,
            color=(255, 255, 255)
        )
        
        initial_pos_x += 51
        lista_b.append(celula)
        id += 1
    
    celulas.append(lista_b)
    initial_pos_y += 51

sprites = pygame.sprite.Group()

while True:
    time = pygame.time.get_ticks()
    
    for row in celulas:
        for celula in row:
            sprites.add(celula)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not start:
            pos = pygame.mouse.get_pos()

            for celula in sprites:
                if celula.rect.collidepoint( pos ):
                    celula.change_status_life()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            start = True

    if start:

        if time % 1000 == 0:
      
            for pos_x in range(0, len(celulas)):
                for pos_y in range(0, len(celulas[0])):
                    celula = celulas[pos_x][pos_y]

                    vecinos = [ vecino for vecino 
                                    in get_vecinos(pos_x, pos_y, celulas) 
                                    if vecino.life == True 
                                    and vecino is not celula]
                        
                    if celula.life:
                
                        if len(vecinos) == 2 or len(vecinos) == 3:
                            print('Sigue vivo')
                        else:
                            celula.change_status_life()

                    else:
                        if len(vecinos) == 3:
                            celula.change_status_life()

            sprites = pygame.sprite.Group()
            for row in celulas:
                for celula in row:
                    sprites.add(celula)

            sprites.draw(surface)

            pygame.display.flip()
            pygame.display.update()

    else:
        sprites.draw(surface)

        pygame.display.flip()
        pygame.display.update()