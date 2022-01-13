import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, x=10, y=10):
    display_surface = pygame.display.get_surface()
    debug_surface = font.render(str(info), True, 'pink')
