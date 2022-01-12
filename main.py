import os
import sys
from level import Level

import pygame

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

level_1_map = ['                                             *************************     ',
               '                                             *************************     ',
               '                                             **                     **     ',
               '                           **                **                     **     ',
               '                          ****               **                     **     ',
               '                      ************           **                     **     ',
               '                    ****************         **                     **     ',
               '                 **********************      **                     **     ',
               '               **************************    *************************     ',
               '  ******      ****************************   *************************     ']

level_1 = Level(screen, level_1_map)

if __name__ == '__main__':
    running = True
    while True:
        delta = 0
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            delta = 5
        if keys[pygame.K_d]:
            delta = -5
        if level_1.left_x + delta <= 0 and level_1.right_x + delta >= 1920:
            level_1.tiles.update(delta)
            level_1.left_x += delta
            level_1.right_x += delta
        level_1.tiles.draw(screen)
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
