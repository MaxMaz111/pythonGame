import pygame
from square import Square


class Level:
    def __init__(self, screen, level_map):
        self.level_map = level_map
        self.screen = screen
        self.tiles = pygame.sprite.Group()
        self.left_x = 0
        self.right_x = 108 * len(level_map[0])
        for i in range(len(self.level_map)):
            for j in range(len(self.level_map[i])):
                if self.level_map[i][j] == '*':
                    Square(j * 108, i * 108, 108, 108, self.tiles)
