import pygame

#This is my first program using pygame.
#This program creates a blank screen with a green rectangle at the bottom of the screen
#The window closes when the user clicks the close button in the window.

GREEN = ( 0, 255, 0)
FPS = 60 # frames per secon
pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sridhar's  first game")
player_gun = pygame.Rect(495,495,30,10)
#Loop until the user clicks the close button

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, GREEN, player_gun)
    clock.tick(FPS)
    pygame.display.update()




pygame.display.flip()
