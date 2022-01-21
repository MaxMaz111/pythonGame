import pygame

import parameters
from button import Button


class MainMenu:
    def __init__(self, screen):
        self.image = None
        self.buttons = pygame.sprite.Group()
        self.screen = screen
        self.timer = 0
        self.animations = [pygame.image.load(f'sprites/idle_left_main_menu/{i}.png') for i in range(4)]
        self.speed = 10
        self.frame = 0
        self.background = pygame.image.load('sprites/back_level.bmp').convert()
        self.new_game = Button(100, 100, 'sprites/new_game.png', 'new', self.buttons)
        self.level_1 = Button(100, 220, 'sprites/level_1.png', '1', self.buttons)
        self.information_btn = Button(1890, 1000, 'sprites/information.png', 'information', self.buttons)
        if parameters.LVL1_COMP:
            self.level_2 = Button(100, 340, 'sprites/level_2.png', '2', self.buttons)
        else:
            self.level_2 = Button(100, 340, 'sprites/level_2wb.png', '2', self.buttons)
        if parameters.LVL2_COMP:
            self.level_3 = Button(100, 460, 'sprites/level_3.png', '3', self.buttons)
        else:
            self.level_3 = Button(100, 460, 'sprites/level_3wb.png', '3', self.buttons)
        if parameters.LVL3_COMP:
            self.finish = Button(100, 580, 'sprites/finish.png', 'finish', self.buttons)

    def run(self):
        if self.timer % self.speed == 0:
            self.frame = (self.frame + 1) % len(self.animations)
            self.image = self.animations[self.frame]
        self.timer += 1
        self.screen.blit(self.background, (0, 0))
        self.buttons.draw(self.screen)
        self.screen.blit(self.image, (600, 400))
        tmp = pygame.image.load('sprites/grass.png')
        for i in range(7):
            self.screen.blit(pygame.transform.scale(tmp, (66 * 5, 66 * 5)), (i * 330, 960))
