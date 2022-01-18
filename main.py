import debug
from button import Button
from level import Level

import pygame

from main_menu import MainMenu
from pause_menu import PauseMenu

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

with open('lvl1.txt', 'r') as f:
    level_1_map = list(map(lambda x: x[:-1], f.readlines()))
with open('lvl2.txt', 'r') as f:
    level_2_map = list(map(lambda x: x[:-1], f.readlines()))
with open('lvl3.txt', 'r') as f:
    level_3_map = list(map(lambda x: x[:-1], f.readlines()))

main_menu = MainMenu(screen)
pause_menu = PauseMenu(screen)
level_1 = Level(screen, level_1_map)
level_2 = Level(screen, level_2_map)
level_3 = Level(screen, level_3_map)
LEVELS = [[main_menu, ], [level_1, level_1_map], [level_2, level_2_map], [level_3, level_3_map], [pause_menu, ]]

PAUSE = False
current_level, last_level = 0, 0
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for i in main_menu.buttons:
                mouse = pygame.mouse.get_pos()
                if i.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    if i.name == 'new':
                        pass
                    if i.name == '1':
                        current_level = 1

                    if i.name == '2':
                        current_level = 2

                    if i.name == '3':
                        current_level = 3

            if current_level == 1:
                for j in level_1.buttons:
                    mouse = pygame.mouse.get_pos()
                    if j.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if j.name == 'pause':
                            last_level = 0 + current_level
                            current_level = 4
                            PAUSE = True
            if current_level == 2:
                for j in level_2.buttons:
                    mouse = pygame.mouse.get_pos()
                    if j.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if j.name == 'pause':
                            last_level = 0 + current_level
                            current_level = 4
                            PAUSE = True
            if current_level == 3:
                for j in level_3.buttons:
                    mouse = pygame.mouse.get_pos()
                    if j.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if j.name == 'pause':
                            last_level = 0 + current_level
                            current_level = 4
                            PAUSE = True
            if current_level == 4:
                for btn in pause_menu.buttons:
                    mouse = pygame.mouse.get_pos()
                    if btn.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if btn.name == 'play':
                            current_level = last_level
                        elif btn.name == 'restart':
                            current_level = 0 + last_level
                            LEVELS[current_level] = [Level(screen, LEVELS[current_level][1]), LEVELS[current_level][1]]
                        elif btn.name == 'back_to_main_menu':
                            current_level = 0

        screen.fill((0, 0, 0))
        LEVELS[current_level][0].run()

        pygame.display.flip()
        clock.tick(60)
pygame.quit()
