import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, elements, x, y, *group):
        super().__init__(*group)
        self.mode = 'idle'
        self.frames = [pygame.transform.scale(pygame.image.load(f'{self.mode}/{i}.png'), (60, 100))
                       for i in range(elements)]
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x * 54 + 24, y * 54 + 8)
        self.mask = pygame.mask.from_surface(self.image)

    def change_mode(self, mode):
        pass

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
