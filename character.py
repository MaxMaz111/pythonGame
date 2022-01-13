import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((50, 50))
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.normal_vector = pygame.math.Vector2(0, 0)
        self.speed_scalar = 10
        self.g = 0.98  # pixels / sec ** 2 ha-ha
        self.jump_impulse = -20
        self.is_jumping = False

    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.normal_vector.x = 1
        elif keys[pygame.K_a]:
            self.normal_vector.x = -1
        else:
            self.normal_vector.x = 0
        if keys[pygame.K_SPACE]:
            if not self.is_jumping:
                self.is_jumping = True
                self.jump()

    def jump(self):
        self.normal_vector.y = self.jump_impulse

    def gravity(self):
        self.normal_vector.y += self.g
        self.rect.y += self.normal_vector.y

    def update(self):
        self.run()
