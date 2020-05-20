import pygame
import UI
import levelBuilder

class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y,type):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Load sprite image
        # self.image = pygame.image.load(filename).convert()
        self.image = pygame.Surface([16,16])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

        self.top = y
        self.left = x


def buildRoom(all_sprites_list):
    wall_list = pygame.sprite.RenderPlain()

    #for i in range(0,16):
    #    wall = Wall(30, 32*i + 64,0)
    #    wall_list.add(wall)
    #    all_sprites_list.add(wall)

    return wall_list




class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.velX = 0
        self.velY = 0

        self.speed = 2

        # Load sprite image
        # self.image = pygame.image.load(filename).convert()
        # self.rect = self.image.get_rect()

        self.homeX = 0
        self.homeY = 0

        #self.prev_x = x;
        #self.prev_y = y;

    def setSpeed(self,x,y):
        self.velX = x
        self.velY = y

    def update(self, walls):

        old_x = self.rect.left
        old_y = self.rect.top;

        new_x = old_x + self.velX
        new_y = old_y + self.velY

        self.rect.left = new_x
        if (pygame.sprite.spritecollide(self, walls, false)):
            self.rect.left = old_x

        self.rect.top = new_y
        if (pygame.sprite.spritecollide(self, walls, false)):
            self.rect.top = new_y


pygame.init()
screen = pygame.display.set_mode((800, 576))
pygame.display.set_caption("Peli xD")
clock = pygame.time.Clock()

def startGame():
    all_sprites_list = pygame.sprite.RenderPlain()
    selector_box = pygame.sprite.RenderPlain()
    wall_list = buildRoom(all_sprites_list)

    done = False
    visualUpdate = True
    mode = 0  # modes: 0=game, 1=levelEditor

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If in level editor

                if levelBuilder.getClickedTile(screen, selector_box):
                    levelBuilder.ColormapToTile.loadRainbowcolors()
                    visualUpdate = True

        if (visualUpdate):

            screen.fill((0,0,0))

            UI.drawGrid(screen)
            UI.drawTopBar(screen)

            all_sprites_list.draw(screen)
            selector_box.draw(screen)

            pygame.display.flip()
            visualUpdate = False
            #print("VisualUpdate")

        clock.tick(10)

startGame()

pygame.quit()