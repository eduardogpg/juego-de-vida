import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def generate_cells(width_screen, height_screen, width_cell, height_cell):
    cells = []

    for pos_x in range(0, width_screen // width_cell):
        rows = []

        for pos_y in range(0, height_screen // height_cell ):
            rows.append(Cell(width_cell, height_cell, pos_x, pos_y))

        cells.append(rows)

    return cells

class Cell(pygame.sprite.Sprite):

    def __init__(self, width, height, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.width = width
        self.height = height

        self.ant = None
        self.check = False

        self.update_rect()
    
    def update_rect(self):
        self.rect = self.get_image()

        self.rect.x = self.pos_x * self.width 
        self.rect.y = self.pos_y * self.height

    def get_image(self):
        self.image = pygame.Surface( (self.width - 1, self.height - 1) )

        if self.ant:
            print('Aqui')
            self.image.fill( self.ant.color )
        
        else:
            if self.check:
                self.image.fill( WHITE )
            else:
                self.image.fill( BLACK )

        return self.image.get_rect()

    def set_ant(self, ant):
        self.ant = ant
        self.update_rect()

    def unset_ant(self):
        self.ant = None
        self.update_rect()

    def set_check(self):
        self.check = not self.check 

        self.update_rect()
