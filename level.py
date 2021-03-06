import pygame

import character
from coin import Coin
from square import Square
from character import Character
from button import Button
from finishsquare import FinishSquare

size = width, height = 1920, 1080


class Level:
    def __init__(self, screen, level_map):
        self.screen = screen
        self.level_map = level_map
        self.tiles = pygame.sprite.Group()
        self.hero = pygame.sprite.GroupSingle()
        self.coins = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.pause_btn = Button(1840, 5, 'sprites/pause.png', 'pause', self.buttons)
        self.coin_display = pygame.image.load('sprites/coin.png')
        self.coin_counter = 0
        self.shift = 0
        self.side = 54
        self.coin_amount = 0
        self.comp = False
        self.dead = False
        self.background = pygame.image.load('sprites/back_level.bmp').convert()
        self.background_rect = self.background.get_rect()
        for i in range(len(self.level_map)):
            for j in range(len(self.level_map[i])):
                if self.level_map[i][j] == '*':
                    Square(j * self.side, i * self.side, self.side, self.side, self.tiles)
                if self.level_map[i][j] == '@':
                    Character(j * self.side, i * self.side, self.hero)
                    self.start_x = j * self.side
                    self.start_y = i * self.side
                if self.level_map[i][j] == 'm':
                    Coin(j * self.side, i * self.side, self.coins)
                    self.coin_amount += 1
                if self.level_map[i][j] == 'f':
                    FinishSquare(j * self.side, i * self.side, self.side, self.side, self.tiles)

    def scroll(self):
        if self.dead:
            return
        if not self.dead:
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
                if i.type == 'finish':
                    self.comp = True
                    return

    def vertical(self):
        self.hero.sprite.gravity()
        for i in self.coins.sprites():
            if i.rect.colliderect(self.hero.sprite.rect):
                self.coins.remove(i)
                self.coin_counter += 1
        for i in self.tiles.sprites():
            if i.rect.colliderect(self.hero.sprite.rect):
                if self.hero.sprite.normal_vector.y > 0:
                    self.hero.sprite.is_jumping = False
                if self.hero.sprite.normal_vector.y < 0:
                    self.hero.sprite.rect.top = i.rect.bottom
                    self.hero.sprite.normal_vector.y = 0
                elif self.hero.sprite.normal_vector.y > 0:
                    self.hero.sprite.rect.bottom = i.rect.top
                    self.hero.sprite.normal_vector.y = 0
                if i.type == 'finish':
                    self.comp = True
                    return
                break
        else:
            self.hero.sprite.is_jumping = True

    def run(self):
        self.screen.blit(self.background, self.background_rect)
        self.tiles.draw(self.screen)
        self.buttons.draw(self.screen)
        self.coins.draw(self.screen)
        font = pygame.font.Font(None, 70)
        text = font.render(f'{self.coin_counter}/{self.coin_amount}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 54
        text_rect.y = 0
        self.screen.blit(text, text_rect)
        self.screen.blit(self.coin_display, (0, 0))
        if not self.dead:
            self.tiles.update(self.shift)
            self.scroll()
            if self.hero.sprite.mode == 'idle_right' or self.hero.sprite.mode == 'idle_left':
                self.hero.sprite.animate(16)
            else:
                self.hero.sprite.animate(6)
            self.hero.update()
            self.horizontal()
            self.vertical()
            self.hero.draw(self.screen)
            self.coins.update(self.shift)

        if self.hero.sprite.rect. y >= height:
            self.dead = True
            character.Character.dead = True
            font = pygame.font.Font(None, 50)
            text = font.render('Game over!', True, (255, 255, 0))
            text_rect = text.get_rect()
            text_rect.centerx = width // 2
            text_rect.centery = height // 2
            self.screen.blit(text, text_rect)
