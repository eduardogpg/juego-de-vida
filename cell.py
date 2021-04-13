import pygame

LIVE = (0, 0, 0)
DEATH = (255, 255, 255)


def generate_cells(width_screen, height_screen, width_cell, height_cell):
    cells = list()

    for pos_x in range(0, height_screen // height_cell ):
        row = list()

        for pos_y in range(0, width_screen // width_cell):

            cell = Cell(width_cell, height_cell, pos_x, pos_y)
            row.append(cell)

        cells.append(row)

    return cells

class Cell(pygame.sprite.Sprite):

    def __init__(self, width, height, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.width = width
        self.height = height

        self.life = False

        self.update_rect()
    
    def update_rect(self):
        self.rect = self.get_image()

        self.rect.x = self.pos_x * self.width 
        self.rect.y = self.pos_y * self.height

    def get_image(self):
        self.image = pygame.Surface( (self.width - 1, self.height - 1) )
        
        if self.life:
            self.image.fill( LIVE )
        else:
            self.image.fill( DEATH )

        return self.image.get_rect()

    def select(self):
        self.life = True
        self.update_rect()