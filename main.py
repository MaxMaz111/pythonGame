import pygame

import parameters
from level import Level
from main_menu import MainMenu
from pause_menu import PauseMenu
from finish_window import FinishWindow

pygame.init()
size = width, height = 1920, 1080

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

with open('lvl1.txt', 'r') as f:
    level_1_map = list(map(lambda x: x[:-1], f.readlines()))
with open('lvl2.txt', 'r') as f:
    level_2_map = list(map(lambda x: x[:-1], f.readlines()))
with open('lvl3.txt', 'r') as f:
    level_3_map = list(map(lambda x: x[:-1], f.readlines()))

main_menu = MainMenu(screen)
level_1 = Level(screen, level_1_map)
level_2 = Level(screen, level_2_map)
level_3 = Level(screen, level_3_map)
pause_menu = PauseMenu(screen)
finish_window = FinishWindow(screen)

stages = [main_menu, level_1, level_2, level_3, pause_menu, finish_window]

pause = False

if __name__ == '__main__':
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if parameters.current_level == 1:
                if stages[parameters.current_level].comp:
                    parameters.LVL1_COMP = True
                    parameters.LVL1_COINS = max(parameters.LVL1_COINS, stages[parameters.current_level].coin_counter)
            if parameters.current_level == 2:
                if stages[parameters.current_level].comp:
                    parameters.LVL2_COMP = True
                    parameters.LVL2_COINS = max(parameters.LVL2_COINS, stages[parameters.current_level].coin_counter)
            if parameters.current_level == 3:
                if stages[parameters.current_level].comp:
                    parameters.LVL3_COMP = True
                    parameters.LVL3_COINS = max(parameters.LVL3_COINS, stages[parameters.current_level].coin_counter)
            for i in stages[parameters.current_level].buttons:
                mouse = pygame.mouse.get_pos()
                if i.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    if i.name == 'pause':
                        pause = True
                        parameters.last_level = parameters.current_level
                        parameters.current_level = 4
                    if i.name == '1':
                        parameters.last_level = 0
                        parameters.current_level = 1
                    if i.name == '2' and parameters.LVL1_COMP:
                        parameters.last_level = 0
                        parameters.current_level = 2
                    if i.name == '3' and parameters.LVL2_COMP:
                        parameters.last_level = 0
                        parameters.current_level = 3
                    if i.name == 'play':
                        parameters.current_level = parameters.last_level
                    if i.name == 'back_to_main_menu':
                        parameters.current_level = 0
                    if i.name == 'restart':
                        parameters.current_level = parameters.last_level
                        stages[parameters.last_level].restart()
                    if i.name == 'new':
                        parameters.LVL1_COMP = False
                        parameters.LVL2_COMP = False
                        parameters.LVL3_COMP = False
                        parameters.LVL1_COINS = 0
                        parameters.LVL2_COINS = 0
                        parameters.LVL3_COINS = 0
        stages[parameters.current_level].run()
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
