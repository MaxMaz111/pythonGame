import os
import sys

from debug import debug
from level import Level

import pygame

pygame.init()
size = width, height = 1200, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

level_map = ['                                                                                                        ',
             '                                                                                                    ****',
             '                                                                               *********    *****   ****',
             '                           **                                                  *********            ****',
             '                          ****                                                                          ',
             '                *     ************                                                                      ',
             '                    ****************                                                    ****            ',
             '             *      ****************                                                    ****            ',
             '                    ****************                                                    ****            ',
             '                    ****************                                                           ******   ',
             '                    ****************                                                           ******   ',
             '                 **********************       ****    ************************************              ',
             '     @         **************************     ****    ************************************              ',
             '  ****** **** ****************************            ************************************              ']

level_1 = Level(screen, level_map)
timer = 0

if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        level_1.run()
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
