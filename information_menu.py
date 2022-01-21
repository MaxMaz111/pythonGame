import pygame
from button import Button

text = ['Цель игры:', 'Собери все монетки и доберись до финиша, он будет помечен травкой.', '\n',
        'Передвижение осуществляется с помощью кнопок a и d - вправо и влево соответственно.',
        'Также можно прыгать нажимая на кнопку пробел']


class InformationMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = pygame.sprite.Group()
        self.information_btn = Button(1890, 70, 'sprites/information.png', 'information1', self.buttons)
        self.font = pygame.font.Font(None, 50)

    def run(self):
        self.buttons.draw(self.screen)
        for i in range(len(text)):
            st = self.font.render(text[i], True, (245, 186, 78))
            self.screen.blit(st, (101, i * 60 + 100))
