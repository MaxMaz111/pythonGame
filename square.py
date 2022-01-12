import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(pygame.image.load('square.png'), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, delta):
        self.rect.x += delta
