import pygame

LIVE = (0, 0, 0)
DEATH = (255, 255, 255)

def generate_cells(width_screen, height_screen, width_cell, height_cell):
    cells = []
    counter = 1

    for pos_x in range(0, width_screen //  width_cell):
        rows = []

        for pos_y in range(0, height_screen // height_cell):

            cell = Cell(counter, width_cell, height_cell, pos_x, pos_y)
            rows.append(cell)
            counter += 1

        cells.append(rows)

    print(len(cells))
    print(len(cells[0]))

    return cells

class Cell(pygame.sprite.Sprite):

    def __init__(self, id, width, height, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.width = width
        self.height = height

        self.life = False
        self.next_life = False

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
        self.life = self.next_life
        self.update_rect()

    def set_next_life(self):
        self.next_life = not self.next_life

    def get_neighborhoods(self, cells):
        neighborhoods = list()
        
        for y in range(self.pos_y -1, self.pos_y + 2):
            for x in range(self.pos_x - 1, self.pos_x + 2):

                if self.pos_x == x and self.pos_y == y:
                   pass
                else:
                    if (x < 0 or y < 0) or (x >= len(cells[0]) or y >= len(cells)):
                        pass
                    else:
                        if cells[x][y].life:
                            neighborhoods.append(cells[x][y])

        return neighborhoods