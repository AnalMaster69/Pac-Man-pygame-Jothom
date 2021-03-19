# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
import random
import world as wo
import player
import enemy



# Setup pygame/window ---------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,32) # windows position
pygame.init()
pygame.display.set_caption('Pac man')
BLOCK_SIZE = 20
SCREEN_WIDTH = 28 * BLOCK_SIZE
SCREEN_HEIGHT = 31 * BLOCK_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()

# Fonts ------------------------------------------------------- #
main_font = pygame.font.SysFont("coopbl", 22)


# Variables ------------------------------------------------------- #


# Constantes -------------------------------------------------------#
START_TIME = pygame.time.get_ticks()

# Classes --------------------------------------------------------- #


# Creation ---------------------------------------------------------#
world = wo.World(SCREEN, BLOCK_SIZE)


# Functions ------------------------------------------------------- #
def redraw():
    SCREEN.fill((22,22,22))


    world.do()


    fps_label = main_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255,200,20))
    SCREEN.blit(fps_label, (5,5))


def buttons():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    pygame.display.update()
    mainClock.tick(90)


# Loop ------------------------------------------------------- #
while True:
    # mouse_x, mouse_y = pygame.mouse.get_pos()
    # pygame.mouse.get_pressed()

     # keys_pressed = pygame.key.get_pressed()
     # if keys_pressed[pygame.K_LEFT]:



    # draw --------------------------------------------- #
    redraw()

    # Buttons ------------------------------------------------ #
    buttons()

    # Update ------------------------------------------------- #
    update()
