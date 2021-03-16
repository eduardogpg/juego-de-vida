import pygame

class Celula(pygame.sprite.Sprite):

    def __init__(self, id, width, height, pos_x, pos_y, color):
        self.id = id

        pygame.sprite.Sprite.__init__(self)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.width = width
        self.height = height

        self.life = False

        self.change_color()

    def change_status_life(self):
        self.life = not self.life
        self.change_color()

    def change_color(self):
        self.image = pygame.Surface( (self.width, self.height) )

        if self.life:
            self.image.fill( (0, 0, 0) )
        else:
            self.image.fill( (255, 255, 255) )

        self.rect = self.image.get_rect()

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
