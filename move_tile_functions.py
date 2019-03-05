import random
import pygame
pygame.init()


#=========================BEGIN Record definition for image record=============================###
#=========================BEGIN Record definition for image record=============================###
class image_record:
    def __init__(self, x_arg, y_arg):
        self.x = x_arg
        self.y = y_arg
        self.image = pygame.image.load('green_tile.png')


#=========================END Record definition for image record=============================###
#=========================END Record definition for image record=============================###


#=========================BEGIN listen_for_quit function=============================###
#=========================BEGIN listen_for_quit function=============================###
def listen_for_quit():
    local_running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            local_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            local_running = False
    return local_running
#=========================END listen_for_quit function=============================###
#=========================END listen_for_quit function=============================###


#=========================BEGIN make_title function=============================###
#=========================BEGIN make_title function=============================###
def make_title(screen):
    # Initialise the text object and associated text rectangle that will hold the heading
    font = pygame.font.Font(None, 36)
    local_title_text = font.render("Leo's Project Move Tiles", 1, (200, 0, 0))
    local_text_rectangle = local_title_text.get_rect()
    local_text_rectangle.centerx = screen.get_rect().centerx
    local_text_rectangle.centery = 30
    return local_title_text, local_text_rectangle
#=========================END make_title function=============================###
#=========================END make_title function=============================###


#=========================BEGIN initialise_tile_list function=============================###
#=========================BEGIN initialise_tile_list function=============================###
def initialise_tile_list(grid_width, tile_width):
    # Create empty list
    local_tile = []
    # use nested list to generate required x and y coords for each record
    j = 0
    while j < grid_width:
        i = 0
        while i < grid_width:
            # call the image_record record constructor passign it i and j multiples of the tile width as x and y coords
            local_tile.append(image_record(
                i * tile_width + 25, j * tile_width + 75))
            i = i + 1
        j = j + 1

    # rescale the images to be 'tile_width' in height and width
    j = 0
    while j < grid_width:
        i = 0
        while i < grid_width:
            local_tile[j * grid_width + i].image = pygame.transform.scale(
                local_tile[j * grid_width + i].image, (tile_width, tile_width))
            i = i + 1
        j = j + 1
    return local_tile
#=========================END initialise_tile_list function=============================###
#=========================END initialise_tile_list function=============================###


#=================================BEGIN draw_tile_list====================================###
#=================================BEGIN draw_tile_list====================================###
def draw_screen(tile, grid_width, title_text, text_rectangle, screen):
    screen.blit(title_text, text_rectangle)
    j = 0
    while j < grid_width:
        i = 0
        while i < grid_width:
            screen.blit(tile[j * grid_width + i].image,
                        (tile[j * grid_width + i].x, tile[j * grid_width + i].y))
            i = i + 1
        j = j + 1

#=================================END draw_tile_list====================================###
#=================================END draw_tile_list====================================###
