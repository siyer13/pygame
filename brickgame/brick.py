import pygame

WHITE = (255,255,255)
GREEN = (20, 255, 140)
RED = (255,0,0)

class Brick(pygame.sprite.Sprite):

    def __init__(self,color,width=10,height=10,x_coord=0,y_coord=0):
        #call the parent class (sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        print(width)
        print(height)
        print(x_coord)
        print(y_coord)
        pygame.draw.rect(self.image,color,[x_coord,y_coord,width,height])

        self.rect = self.image.get_rect()
