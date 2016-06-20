import pygame
from brick import Brick





def construct_wall():
    for rect_y in range(1,40,10) :
        for rect_x in range(1,400,10):
            wall = all_sprites_list.add(draw_brick(9,9,rect_x,rect_y))
    return wall;



pygame.init()

GREEN = (20, 255, 140)
RED = (255,0,0)

SCREENWIDTH=400
SCREENHEIGHT=500

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Game")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()



#brick = Brick(GREEN,20,20,50,60)
#brick1 = Brick(GREEN,30,30,20,10)
#brick2 = Brick(GREEN,10,10,120,120)
#brick3 = Brick(RED,20,20,10,20)

bricku = Brick(GREEN,30,30,120,120)

all_sprites_list.add(bricku)

carryOn = True
clock=pygame.time.Clock()

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        #Refresh Screen
        pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)
pygame.quit()
