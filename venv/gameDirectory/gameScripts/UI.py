import pygame
import math

WIDTH = 800
HEIGHT = 576
TOP_GAP = 64
ARENA_SIZE = 512

white = [255,255,255]
itemBox = pygame.image.load("../assets/box_2.png")
backGround = pygame.image.load("../assets/background.png");
#font = pygame.font.SysFont(None, 32)

def drawGrid(screen):
    # Height is 576 with 32 high upper bar
    # Width is xxx
    #pygame.draw.line(screen, white, [32, TOP_GAP+1], [WIDTH-32, TOP_GAP+1])
    #pygame.draw.line(screen, white, [32, TOP_GAP], [WIDTH-32, TOP_GAP])

    #screen.blit(lineEndL, (0, TOP_GAP-30))
    #screen.blit(lineEndR, (WIDTH-32, TOP_GAP-32))

    #pygame.draw.line(screen, white, [ARENA_SIZE+1, 32], [ARENA_SIZE+1, HEIGHT-32])
    #pygame.draw.line(screen, white, [ARENA_SIZE, 32], [ARENA_SIZE, HEIGHT-32])

    #screen.blit(lineEndU, (ARENA_SIZE-32, 0))
    #screen.blit(lineEndD, (ARENA_SIZE-30, HEIGHT-32))

    #screen.blit(lineMiddle, (ARENA_SIZE - 30, TOP_GAP-30))
    screen.blit(backGround, (0,0))

def drawTopBar(screen):
    itemCount = 4 # max 4
    itemWidth = 32+32+32
    gap = math.floor((ARENA_SIZE - itemCount*itemWidth) / (itemCount+1))

    #itemBox.convert()
    #itemBoxRect = itemBox.get_rect()

    for i in range(1, itemCount+1):
        # Jokainen data-alkio päivitetään
        newX = i*gap + (i-1)*itemWidth
        #print("D ", itemBoxRect.x, " , ", itemBoxRect.y)
        #pygame.draw.rect(screen, white, pygame.Rect(newX, 16, itemWidth, 32))
        #itemBoxRect.move(gap*i, 10)
        screen.blit(itemBox, (newX, 12))
        #pygame.display.flip()
        # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))