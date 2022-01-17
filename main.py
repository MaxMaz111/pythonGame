import debug
from button import Button
from level import Level

import pygame

from main_menu import MainMenu

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

level_1_map = ['**********************************************************************************************************************************',
               '*                                                                                                                                *',
               '*                                                                                                                                *',
               '*                                                                                                                                *',
               '*                                                                                                                                *',
               '*                                                                                                                                *',
               '*                                                                                                                                *',
               '*                                                                                                                                *',
               '*                                                                                                                                *',
               '*                                                                m                                                               *',
               '*                       ********                               *******                                                           *',
               '*                                 *********       ****                                                                         * *',
               '*     @           *****                    *     **        **             *****                                         *****    *',
               '*          ****                           **     *      ***                                 **                     ****          *',
               '*                                         *      *              *******         ******                  *******                  *',
               '*   ****                        ****      *    ***                                    ***       *****   *******                  *',
               '*      **                      *    *     *                 ****                      *  *              ******* *                *',
               '****     *                    *      *   ***               *                          *                 *******    *             *',
               '* *** m                      *        *m   *      m                                    *                m*******    *            *',
               '********************************************  *************                    ***************************************************']

level_2_map = ['*************************************************************************************************',
               '*                                                                      *****                    *',
               '*                                                                                               *',
               '*        ******                                                                                 *',
               '*                m                             m  **                                            *',
               '*                *            ******         ****    **        *****                            *',
               '*  ***                                                              **        ********       m  *',
               '*                 ******              *******              m                m             *******',
               '**                             m                         *****            **** *                *',
               '*        *****              *******                                      *                      *',
               '* m                                             ******                                          *',
               '* *****            ******                                                                       *',
               '*                                     ***                           ***********           *******',
               '*       @                            ***********                                                *',
               '*     **********     m                                    *******                   m           *',
               '*                    *        ******                                 m          *********       *',
               '*                                                *******          ******                        *',
               '*                         **          ********                                                  *',
               '*    *******  *  ******                                                                         *',
               '***                                                                                             *']

level_3_map = ['',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '',
               '']

main_menu = MainMenu(screen)
level_1 = Level(screen, level_1_map)
level_2 = Level(screen, level_2_map)
level_3 = Level(screen, level_3_map)
current_level = 0
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
                        
        screen.fill((0, 0, 0))
        if current_level == 0:
            main_menu.run()
        elif current_level == 1:
            level_1.run()
        elif current_level == 2:
            level_2.run()
        elif current_level == 3:
            level_3.run()
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
