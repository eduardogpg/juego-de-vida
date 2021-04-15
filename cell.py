import pygame

LIVE = (0, 0, 0)
DEATH = (255, 255, 255)

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

    def update(self):
        self.life = self.next_life
        self.update_rect()

    def change(self):
        self.next_life = not self.next_life

    def select(self):
        self.change()
        self.update()

    def restar(self):
        self.next_life = False
        self.life = False
        self.change()

    def get_neighborhoods(self, cells):
        neighborhoods = list()
        
        for x in range(self.pos_x -1, self.pos_x + 2):
            for y in range(self.pos_y - 1, self.pos_y + 2):
               
               if (x >= 0 and y >= 0) and (x < len(cells) and y < len(cells[0]) ):

                    if not(x == self.pos_x and y == self.pos_y) and cells[x][y].life:
                       neighborhoods.append(cells[x][y]) 

        return neighborhoods