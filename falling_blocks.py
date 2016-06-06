import pygame
import random

#This is my first program using pygame.
#This program creates a blank screen with a green rectangle at the bottom of the screen
#The window closes when the user clicks the close button in the window.

GREEN = ( 0, 255, 0)
BLACK = (0,0,0,)
FPS = 60 # frames per secon
pygame.init()
x = 495
y = 495
x_x = 2
y_y = 0
count = 1
size = (700,500)
new = 1
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Falling blocks")

#Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

def create_blocks(x_x,y_y,count,new):
    screen.fill(BLACK)
    if new:
        for i in range(count):

            asteroid = pygame.Rect(x_x, y_y, 10,10)
            x_x = random.randrange(2,490)
            pygame.draw.rect(screen,GREEN,asteroid)


while not done:
    y_y += 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Closing")
            done = True
    if y_y > 490:
        y_y = 0
        x_x = random.randrange(2,495)
        new = 1
        count += 1

    #screen.fill(BLACK)
    print(count)
    create_blocks(x_x,y_y, count,new)
    new = 1
    clock.tick(FPS)

    pygame.display.update()

#
pygame.display.flip()
