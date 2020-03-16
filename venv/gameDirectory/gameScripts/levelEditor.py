#TODO: Change tile
import pygame
import math
WIDTH = 800
HEIGHT = 576
TOP_GAP = 64
ARENA_SIZE = 512

selectBox = pygame.image.load("../assets/selectBox.png");

def getClickedTile():
    tile_x = 0
    tile_y = 0
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_x <= ARENA_SIZE and mouse_y > TOP_GAP:
        tile_x = math.floor(mouse_x/ARENA_SIZE)
        tile_y = math.floor((mouse_y-TOP_GAP)/ARENA_SIZE)
    else:
        return

    screen.blit(selectBox, (tile_x, tile_y))
