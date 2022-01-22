import pygame
from button import Button

text = ['Цель игры:', '    Собери все монетки и доберись до финиша, он будет помечен травкой.', ' ',
        'Передвижение осуществляется с помощью кнопок a и d - вправо и влево соответственно.',
        'Также можно прыгать нажимая на кнопку пробел',
        'После прохождения всех уровней можно будет завершить игру, сохранив результат.',
        'Для этого нужно ввести ник. Он может состоять только из английских и/или русских букв и цифр,',
        'если будет введен недопустимый символ, то его не будет в никнейме',
        '                                        Собери как можно больше монеток и побей рекорд']


class InformationMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = pygame.sprite.Group()
        self.information_btn = Button(1860, 70, 'sprites/information.png', 'information1', self.buttons)
        self.font = pygame.font.Font(None, 50)

    def run(self):
        self.buttons.draw(self.screen)
        for i in range(len(text)):
            st = self.font.render(text[i], True, (245, 186, 78))
            self.screen.blit(st, (101, i * 60 + 100))
