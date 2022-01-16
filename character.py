import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.animations = {'idle_right': [pygame.image.load(f'idle_right/{i}.png') for i in range(4)],
                           'idle_left': [pygame.image.load(f'idle_left/{i}.png') for i in range(4)],
                           'run_right': [pygame.image.load(f'run_right/{i}.png') for i in range(8)],
                           'run_left': [pygame.image.load(f'run_left/{i}.png') for i in range(8)],
                           'jump_right': [pygame.image.load(f'jump_right/0.png') for i in range(1)],
                           'jump_left': [pygame.image.load(f'jump_left/0.png') for i in range(1)]}
        self.mode = 'idle_right'
        self.frame = 0
        self.image = self.animations[self.mode][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.normal_vector = pygame.math.Vector2(0, 0)
        self.speed_scalar = 10
        self.g = 0.98
        self.jump_impulse = -25
        self.is_jumping = False
        self.timer = 0

    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not self.is_jumping:
                self.is_jumping = True
                if 'right' in self.mode:
                    self.mode = 'jump_right'
                elif 'left' in self.mode:
                    self.mode = 'jump_left'
                self.jump()
            if keys[pygame.K_d]:
                self.normal_vector.x = 1
            elif keys[pygame.K_a]:
                self.normal_vector.x = -1
            else:
                self.normal_vector.x = 0
        elif keys[pygame.K_d]:
            self.normal_vector.x = 1
            self.mode = 'run_right'
        elif keys[pygame.K_a]:
            self.normal_vector.x = -1
            self.mode = 'run_left'
        else:
            self.normal_vector.x = 0
            if 'right' in self.mode:
                self.mode = 'idle_right'
            elif 'left' in self.mode:
                self.mode = 'idle_left'

    def animate(self, speed):
        if self.timer % speed == 0:
            self.frame = (self.frame + 1) % len(self.animations[self.mode])
            self.image = self.animations[self.mode][self.frame]
        self.timer += 1

    def jump(self):
        self.normal_vector.y = self.jump_impulse

    def gravity(self):
        self.normal_vector.y += self.g
        self.rect.y += self.normal_vector.y

    def update(self):
        self.run()
