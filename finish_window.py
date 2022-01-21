import pygame

import parameters
from button import Button


class FinishWindow:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = pygame.sprite.Group()
        self.input_btn = Button(1300, 450, 'sprites/input.png', 'input', self.buttons)
        self.make_table_btn = Button(20, 700, 'sprites/make_table.png', 'make_table', self.buttons)
        self.new_game_btn = Button(700, 700, 'sprites/new_game.png', 'new', self.buttons)
        font = pygame.font.Font(None, 50)
        self.text = font.render(parameters.text, True, (0, 255, 255))
        self.text2 = font.render('Введите ник:', True, (255, 255, 255))

    def run(self):
        self.buttons.draw(self.screen)
        pygame.draw.line(self.screen, (255, 255, 255), (100, 650), (1000, 650), width=3)
        self.screen.blit(self.text2, (20, 300))
        self.screen.blit(self.text, (101, 599))
