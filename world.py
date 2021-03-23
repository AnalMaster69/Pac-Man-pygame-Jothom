import pygame
import level as lv



class World:
    def __init__(self, SCREEN, BLOCK_SIZE):
        # SCREEN_WIDTH = SCREEN.get_width()
        # SCREEN_HEIGHT = SCREEN.get_height()
        self.SCREEN = SCREEN
        self.BLOCK_SIZE = BLOCK_SIZE

        self.current_level = 2


    def draw(self):
        obstacles_color = (12, 66, 222)

        level = lv.all_levels[self.current_level]

        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == 1:# if obstacle
                    pygame.draw.rect(self.SCREEN,obstacles_color, (x*self.BLOCK_SIZE, y*self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))


    def do(self):
        """make the world functional"""
        self.draw()
