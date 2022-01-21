import pygame
from button import Button


class FinishWindow:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = pygame.sprite.Group()
        self.input_btn = Button(1300, 450, 'sprites/input.png', 'input', self.buttons)
        self.make_table_btn = Button(20, 700, 'sprites/make_table.png', 'make_table', self.buttons)
        self.new_game_btn = Button(700, 700, 'sprites/new_game.png', 'new', self.buttons)

    def run(self):
        self.buttons.draw(self.screen)
