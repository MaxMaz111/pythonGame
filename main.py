import os
import sys
from level import Level
from character import Character

import pygame

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

level_1_map = ['                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                      ',
               '                                                                                                  ****',
               '                                                                                                  ****',
               '                           **                                                                     ****',
               '                          ****                                                                        ',
               '                      ************                                                                    ',
               '                    ****************                                                                  ',
               '                 **********************                                                               ',
               '               **************************                                                             ',
               '  ******      ****************************                                                            ']

level_1 = Level(screen, level_1_map)

hero_group = pygame.sprite.GroupSingle()
hero = Character(4, 5, 18, hero_group)
timer = 0

v_x = 0
v_y = 0

if __name__ == '__main__':
    running = True
    while True:
        timer += 1
        v_x = 0
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            v_x = -5
        if keys[pygame.K_d]:
            v_x = 5
        if (width // 2 - 10) <= hero.rect.x <= (width // 2 + 10) and \
                ((level_1.left_x + v_x >= 0 and v_x < 0) or (level_1.right_x < 54 * len(level_1_map[0]) and v_x > 0)) \
                and not pygame.sprite.spritecollide(hero, level_1.tiles, False):
            level_1.tiles.update(-v_x)
            level_1.left_x += v_x
            level_1.right_x += v_x
        elif 0 <= hero.rect.x + v_x <= 1920 and not pygame.sprite.spritecollide(hero, level_1.tiles, False):
            hero.rect.x += v_x
        if pygame.sprite.spritecollide(hero, level_1.tiles, False):
            hero.rect.x -= v_x
        if timer % 16 == 0:
            hero.update()
        hero_group.draw(screen)
        level_1.tiles.draw(screen)
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
