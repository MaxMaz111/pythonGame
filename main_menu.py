import pygame

import parameters
from button import Button


class MainMenu:
    def __init__(self, screen):
        self.buttons = pygame.sprite.Group()
        self.screen = screen
        self.new_game = Button(100, 100, 'sprites/new_game.png', 'new', self.buttons)
        self.level_1 = Button(100, 220, 'sprites/level_1.png', '1', self.buttons)
        if parameters.LVL1_COMP:
            self.level_2 = Button(100, 340, 'sprites/level_2.png', '2', self.buttons)
        else:
            self.level_2 = Button(100, 340, 'sprites/level_2wb.png', '2', self.buttons)
        if parameters.LVL2_COMP:
            self.level_3 = Button(100, 460, 'sprites/level_3.png', '3', self.buttons)
        else:
            self.level_3 = Button(100, 460, 'sprites/level_3wb.png', '3', self.buttons)

    def run(self):
        self.buttons.draw(self.screen)
