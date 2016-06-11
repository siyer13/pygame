import pygame
import random

#This is my first program using pygame.
#This program creates a blank screen with a green rectangle at the bottom of the screen
#The window closes when the user clicks the close button in the window.

GREEN = ( 0, 255, 0)
BLACK = (0,0,0,)
FPS = 60 # frames per secon
pygame.init()
gun_x = 495
gun_y = 495
x_x = 2
y_y = 0
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sridhar's  first game")
#player_gun = pygame.Rect(x,y,30,10)
#Loop until the user clicks the close button



done = False
clock = pygame.time.Clock()

while not done:
    y_y += 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Closing")
            done = True
        if event.type == pygame.KEYDOWN:
            print("Keyed down")
            if event.key == pygame.K_LEFT:
                print("Left key pressed")
                gun_x -= 40
            if event.key == pygame.K_RIGHT:
                print("Right key pressed")
                gun_x += 40
            if event.key == pygame.K_DOWN:
                print("Down key pressed")
                #gun_y += 20
            if event.key == pygame.K_UP:
                print("Up key pressed")
                gun_y -= 20
    if y_y > 490:
        y_y = 0
        x_x = random.randrange(2,695)


    screen.fill(BLACK)



    for y in range(2,40,11) :
        for x in range(2,700,11):
            asteroid = pygame.Rect(x,y, 10,10)
            pygame.draw.rect(screen,GREEN,asteroid)




    pygame.draw.rect(screen,GREEN,asteroid)
    falling_asteroid = pygame.Rect(x_x, y_y, 10,10)
    player_gun = pygame.Rect(gun_x,gun_y,50,10)
    pygame.draw.rect(screen, GREEN, player_gun)
    pygame.draw.rect(screen,GREEN,falling_asteroid)
    clock.tick(FPS)
    pygame.display.update()



#
pygame.display.flip()
