import pygame

from button import Button


class PauseMenu:
    def __init__(self, screen):
        self.buttons = pygame.sprite.Group()
        self.screen = screen
        self.continue_btn = Button(870, 513, 'sprites/play.png', 'play', self.buttons)
        self.restart_btn = Button(710, 600, 'sprites/restart.png', 'restart', self.buttons)
        self.back_to_main_menu_btn = Button(920, 600, 'sprites/back_to_main_menu.png', 'back_to_main_menu', self.buttons)

    def run(self):
      #  self.screen.fill((0, 0, 0))
        self.buttons.draw(self.screen)
