import pygame

class Ant(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.last_cell = None

        self.color = (168, 56, 148)

    """
        Si está sobre un cuadrado blanco, cambia el color del cuadrado,
        gira noventa grados a la izquierda y avanza un cuadrado.
        
        Si está sobre un cuadrado negro, cambia el color del cuadrado,
        gira noventa grados a la derecha y avanza un cuadrado.
    """

    def check(self, cells):
        current_cell = cells[self.pos_x][self.pos_y]
        current_cell.set_ant(self)

        # Algortimo
        self.pos_x -= 1 

        # current_cell.set_check()
        
        if self.last_cell:
            self.last_cell.unset_ant()

        self.last_cell = current_cell