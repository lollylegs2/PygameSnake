from move_tile_functions import *
import pygame
from snake import *


pygame.init()


# Set dimensions for screen, tiles and grid

screenWidth = 600
screenHeight = 650
screenColor = (0, 0, 0)
gridWidth = 50
tileWidth = int((screenWidth - 50)/gridWidth)

# initiate clock and screen objects

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))

# generate the list of records to hold Tiles
tile = initialise_tile_list(gridWidth, tileWidth)

# Make the heading
titleText, textRectangle = make_title(screen)

snake = snake(40, 40, 1)


running = True
while running == True:
    clock.tick(30)
    running = listen_for_quit()
    screen.fill(screenColor)
    key = pygame.key.get_pressed()
    snake.updateSnake(key, screen)
    # draw to screen the heading and list/array
    draw_screen(tile, gridWidth, titleText, textRectangle, screen)

    pygame.display.flip()


pygame.display.quit()
