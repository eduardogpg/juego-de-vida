import pygame

class Ant(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):

        pygame.sprite.Sprite.__init__(self)

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.color = (168, 56, 148)

    