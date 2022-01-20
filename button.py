import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, name,  *group):
        super().__init__(*group)
        self.name = name
        im = pygame.image.load(image)
        self.image = pygame.transform.scale(im, (im.get_width(), im.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
