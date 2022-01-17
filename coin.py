import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super(Coin, self).__init__(*group)
        self.image = pygame.image.load('sprites/coin.png')
        self.type = 'coin'
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = (54, 54)

    def update(self, delta):
        self.rect.x += delta
