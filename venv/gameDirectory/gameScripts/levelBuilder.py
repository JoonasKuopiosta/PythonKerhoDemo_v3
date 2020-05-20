#TODO: Change tile
import pygame
import math
import bpy
WIDTH = 800
HEIGHT = 576
TOP_GAP = 64
ARENA_SIZE = 512
TILE_SIZE = 32

#selectBox = pygame.image.load("../assets/selectBox.png");

class ColormapToTiles:
    rainbowColors = []

    def __init__(self):
        #asd
        pass

    def loadRainbowColors(self):
        image_file = '../miscs/color_rainbow.bmp'
        image = bpy.data.images[image_file]
        print(image)


class SelectBox(pygame.sprite.Sprite):

    def __init__(self,tile_x,tile_y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Load sprite image
        self.image = pygame.image.load("../assets/selectBox.png")

        self.rect = self.image.get_rect()
        self.rect.top = tile_y*TILE_SIZE+TOP_GAP
        self.rect.left = tile_x*TILE_SIZE

        self.top = tile_y*TILE_SIZE+TOP_GAP
        self.left = tile_x*TILE_SIZE

def getClickedTile(screen, selector_box):
    tile_x = 0
    tile_y = 0
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_x <= ARENA_SIZE and mouse_y > TOP_GAP:
        tile_x = math.floor(mouse_x/TILE_SIZE)
        tile_y = math.floor((mouse_y-TOP_GAP)/TILE_SIZE)
    else:
        return False

    selector_box.empty() # Edellinen poistetaan
    selector_box.add(SelectBox(tile_x, tile_y))
    return True
