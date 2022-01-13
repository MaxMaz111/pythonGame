import pygame
from square import Square
from character import Character

size = width, height = 1200, 700


class Level:
    def __init__(self, screen, level_map):
        self.screen = screen
        self.level_map = level_map
        self.tiles = pygame.sprite.Group()
        self.hero = pygame.sprite.GroupSingle()
        self.shift = 0
        self.side = 50
        for i in range(len(self.level_map)):
            for j in range(len(self.level_map[i])):
                if self.level_map[i][j] == '*':
                    Square(j * self.side, i * self.side, self.side, self.side, self.tiles)
                if self.level_map[i][j] == '@':
                    Character(j * self.side, i * self.side, self.hero)

    def scroll(self):
        if self.hero.sprite.rect.centerx < width // 5 and self.hero.sprite.normal_vector.x < 0:
            self.shift = 5
            self.hero.sprite.speed_scalar = 0
        elif self.hero.sprite.rect.centerx > width * 4 // 5 and self.hero.sprite.normal_vector.x > 0:
            self.shift = -5
            self.hero.sprite.speed_scalar = 0
        else:
            self.shift = 0
            self.hero.sprite.speed_scalar = 5

    def horizontal(self):
        self.hero.sprite.rect.x += self.hero.sprite.normal_vector.x * self.hero.sprite.speed_scalar
        for i in self.tiles.sprites():
            if i.rect.colliderect(self.hero.sprite.rect):
                if self.hero.sprite.normal_vector.x < 0:
                    self.hero.sprite.rect.left = i.rect.right
                elif self.hero.sprite.normal_vector.x > 0:
                    self.hero.sprite.rect.right = i.rect.left

    def vertical(self):
        self.hero.sprite.gravity()
        for i in self.tiles.sprites():
            if i.rect.colliderect(self.hero.sprite.rect):
                self.hero.sprite.is_jumping = False
                if self.hero.sprite.normal_vector.y < 0:
                    self.hero.sprite.rect.top = i.rect.bottom
                    self.hero.sprite.normal_vector.y = 0
                elif self.hero.sprite.normal_vector.y > 0:
                    self.hero.sprite.rect.bottom = i.rect.top
                    self.hero.sprite.normal_vector.y = 0

    def run(self):
        self.tiles.update(self.shift)
        self.tiles.draw(self.screen)
        self.scroll()

        self.hero.update()
        self.horizontal()
        self.vertical()
        self.hero.draw(self.screen)
