import pygame
import level as lv
import time


class Player:
    def __init__(self, SCREEN, BLOCK_SIZE):
        self.SCREEN = SCREEN
        self.BLOCK_SIZE = BLOCK_SIZE
        self.move_speed = 0.2 # the player will move every x sec
        self.move_timer = 0 # timer tostore the player move time

        self.reset()




    def reset(self):
        self.position = {"x":1, "y":1}
        self.direction = (0, 0)
        self.new_direction = None


    def draw(self):
        color = (222, 200, 33)
        #print(self.position["y"]*self.BLOCK_SIZE + self.BLOCK_SIZE//2)
        pygame.draw.circle(self.SCREEN,color,(self.position["x"]*self.BLOCK_SIZE + self.BLOCK_SIZE//2, self.position["y"]*self.BLOCK_SIZE + self.BLOCK_SIZE//2), self.BLOCK_SIZE//2)


    def change_direction(self):

        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT]:
            self.new_direction = (-1,0)

        if keyPressed[pygame.K_RIGHT]:
            self.new_direction = (1,0)

        if keyPressed[pygame.K_UP]:
            self.new_direction = (0,-1)

        if keyPressed[pygame.K_DOWN]:
            self.new_direction = (0,1)




    def move(self):
        self.change_direction()

        if time.time() > self.move_timer:
            print("should move")
            self.move_timer = time.time() + self.move_speed

            # test if the new direction is valid
            if self.new_direction != None:
                if lv.all_levels[1][self.position["y"] + self.new_direction[1]][self.position["x"] + self.new_direction[0]] != 1:
                    self.direction = self.new_direction


            # move the player
            nextCase = lv.all_levels[1][self.position["y"] + self.direction[1]][self.position["x"] + self.direction[0]]

            if nextCase != 1:
                self.position["x"] = self.position["x"] + self.direction[0]
                self.position["y"] = self.position["y"] + self.direction[1]





    def do(self):
        """make the player functional"""
        self.draw()
        self.move()
