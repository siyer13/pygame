import pygame

#This is my first program using pygame.
#This program creates a blank screen with a green rectangle at the bottom of the screen
#The window closes when the user clicks the close button in the window.

GREEN = ( 0, 255, 0)
BLACK = (0,0,0,)
FPS = 60 # frames per secon
pygame.init()
x = 495
y = 495
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sridhar's  first game")
#player_gun = pygame.Rect(x,y,30,10)
#Loop until the user clicks the close button

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Closing")
            done = True
        if event.type == pygame.KEYDOWN:
            print("Keyed down")
            if event.key == pygame.K_LEFT:
                print("Left key pressed")
                x -= 10
            if event.key == pygame.K_RIGHT:
                print("Right key pressed")
                x += 10
            if event.key == pygame.K_DOWN:
                print("Down key pressed")
                y += 10
            if event.key == pygame.K_UP:
                print("Up key pressed")
                y -= 10

    screen.fill(BLACK)
    player_gun = pygame.Rect(x,y,30,10)
    pygame.draw.rect(screen, GREEN, player_gun)
    clock.tick(FPS)
    pygame.display.update()



#
pygame.display.flip()
