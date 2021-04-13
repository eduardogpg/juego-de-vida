import pygame

DEATH = (0, 0, 0)
LIVE = (255, 255, 255)

def generate_cells(width_screen, height_screen, width_cell, height_cell):
    cells = list()
    current_pos_y = 1

    for _ in range(0, height_screen // height_cell ):
        row = list()
        current_pos_x = 0

        for _ in range(0, width_screen // width_cell):

            cell = Cell(width_cell, height_cell, current_pos_x, current_pos_y)
            current_pos_x = current_pos_x + 1 + width_cell

            row.append(cell)

        current_pos_y = current_pos_y + 1 + height_cell
        cells.append(row)

    print(len(cells[0]))
    print(len(cells))

    return cells

class Cell(pygame.sprite.Sprite):

    def __init__(self, width, height, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.width = width
        self.height = height

        self.life = True

        self.update_rect()
    
    def update_rect(self):
        self.rect = self.get_image()

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def get_image(self):
        self.image = pygame.Surface( (self.width, self.height) )
        self.image.fill( LIVE )
        
        return self.image.get_rect()