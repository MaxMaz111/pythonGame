import pygame

import csv
import datetime
import sqlite3
from level import Level
from main_menu import MainMenu
from pause_menu import PauseMenu
from finish_window import FinishWindow
import parameters
from parameters import current_level, last_level
from information_menu import InformationMenu

pygame.init()
size = width, height = 1920, 1080

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background = pygame.image.load('sprites/back_level.png')
screen.blit(background, (0, 0, 1920, 1080))
con = sqlite3.connect('Leaderboard.db')
cur = con.cursor()

with open('lvl1.txt', 'r') as f:
    level_1_map = list(map(lambda x: x[:-1], f.readlines()))
with open('lvl2.txt', 'r') as f:
    level_2_map = list(map(lambda x: x[:-1], f.readlines()))
with open('lvl3.txt', 'r') as f:
    level_3_map = list(map(lambda x: x[:-1], f.readlines()))

information_menu = InformationMenu(screen)
main_menu = MainMenu(screen)
level_1 = Level(screen, level_1_map)
level_2 = Level(screen, level_2_map)
level_3 = Level(screen, level_3_map)
pause_menu = PauseMenu(screen)
finish_window = FinishWindow(screen)

LEVELS = [[main_menu, ],
          [level_1, level_1_map], [level_2, level_2_map], [level_3, level_3_map],
          [pause_menu, ],
          [finish_window, ],
          [information_menu, ]]
# уровень, карта
PAUSE = False
tmpcomplvl = False
parameters.text = ''

if __name__ == '__main__':
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if current_level == 0:
                for i in main_menu.buttons:
                    mouse = pygame.mouse.get_pos()
                    if i.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if i.name == 'information':
                            current_level = 6
                        if i.name == 'new':
                            current_level = 0
                            parameters.LVL1_COMP = False
                            parameters.LVL2_COMP = False
                            parameters.LVL3_COMP = False
                            LEVELS[0][0] = MainMenu(screen)
                        if i.name == '1':
                            current_level = 1
                            tmpcomplvl = 0 + level_1.comp
                            LEVELS[current_level][0] = level_1 = Level(screen, level_1_map)
                        if i.name == '2' and parameters.LVL1_COMP:
                            current_level = 2
                            mpcomplvl = 0 + level_2.comp
                            LEVELS[current_level][0] = level_2 = Level(screen, level_2_map)
                        if i.name == '3' and parameters.LVL2_COMP:
                            current_level = 3
                            mpcomplvl = 0 + level_3.comp
                            LEVELS[current_level][0] = level_3 = Level(screen, level_3_map)
                        if i.name == 'finish':
                            current_level = 5

            if current_level == 1:
                for j in level_1.buttons:
                    mouse = pygame.mouse.get_pos()
                    if j.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if j.name == 'pause':
                            last_level = 0 + current_level
                            current_level = 4
                            PAUSE = True
                if level_1.comp:
                    current_level = 0
                    main_menu = MainMenu(screen)
                    LEVELS[0] = [main_menu, ]
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
                            tmpcomp = max(LEVELS[last_level][0].comp, tmpcomplvl)
                            LEVELS[last_level] = [Level(screen, LEVELS[last_level][1]), LEVELS[last_level][1]]
                            LEVELS[last_level][0].comp = tmpcomp
                            current_level = 0
            if current_level == 5:
                inputflag = True
                pygame.key.start_text_input()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    if parameters.text:
                        parameters.text = parameters.text[:-1]
                elif event.type == pygame.KEYDOWN and inputflag and event.unicode != '\x08':
                    if len(parameters.text) <= 20:
                        parameters.text += event.unicode
                    else:
                        if not inputflag:
                            pygame.key.stop_text_input()
                        inputflag = False
                LEVELS[current_level][0] = FinishWindow(screen)
                for btn in finish_window.buttons:
                    mouse = pygame.mouse.get_pos()
                    if btn.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if btn.name == 'input':
                            if parameters.text:
                            # cur.execute(f'INSERT INTO table(name, score) VALUES({parameters.text}, {score})')
                                pass
                        elif btn.name == 'make_table':
                            res = cur.execute(f'SELECT * FROM table1').fetchall()
                            res.sort(key=lambda x: x[1])
                            fname = datetime.datetime.now().strftime("%H.%M.%S  %d.%m.%Y") + ' scoreboard'
                            with open(f'{fname}.csv', 'w', encoding='utf8') as f:
                                writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                for i in res:
                                    writer.writerow(i)
                        elif btn.name == 'new':
                            parameters.text = ''
                            current_level = 0
                            parameters.LVL1_COMP = False
                            parameters.LVL2_COMP = False
                            parameters.LVL3_COMP = False
                            LEVELS[0][0] = MainMenu(screen)
                            break
            if current_level == 6:
                for btn in information_menu.buttons:
                    mouse = pygame.mouse.get_pos()
                    if btn.rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if btn.name == 'information1':
                            current_level = 0
        parameters.current_level = current_level
        parameters.last_level = last_level
        screen.fill((0, 0, 0))
        LEVELS[current_level][0].run()
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
