import pygame

class Ant(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.orientacion = 12
        self.last_cell = None

        self.color = (168, 56, 148)

    def check(self, cells):
        current_cell = cells[self.pos_x][self.pos_y]
        current_cell.set_ant(self)

        if current_cell.check:
            self.orientacion -= 3
            if self.orientacion <= 0:
                self.orientacion = 12

        else:
            self.orientacion += 3
            if self.orientacion > 12:
                self.orientacion = 3
            
        if self.orientacion == 3:
            self.pos_x += 1
        elif self.orientacion == 6:
            self.pos_y += 1
        elif self.orientacion == 9:
            self.pos_x -= 1
        elif self.orientacion == 12:
            self.pos_y -= 1

        current_cell.set_check()
        
        if self.last_cell:
            self.last_cell.unset_ant()

        self.last_cell = current_cell