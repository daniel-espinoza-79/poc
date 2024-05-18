# Example file showing a basic pygame "game loop"
import pygame
#from sys import exit
import os
from enum import Enum

FPS = 60


class Movement(Enum):
    LEFT = 0
    RIGHT = 1

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Running Game")
clock = pygame.time.Clock()
running = True
sky_image  = pygame.image.load(os.getcwd()+'/graphics/Sky.png')
ground     = pygame.image.load(os.getcwd()+'/graphics/ground.png')


test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("My Game", False , 'Green')


snail_surface = pygame.image.load(os.getcwd()+"/graphics/snail/snail1.png").convert_alpha()

snail_x_pos = 600 
snail_y_pos = 265

move = Movement.LEFT

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #exit() this is a good idea

    # fill the screen with a color to wipe away anything from last frame

    screen.blit(sky_image, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(text_surface, (350, 50)) 
    
    if move == Movement.LEFT:
        if snail_x_pos > 0:
            snail_x_pos-=10
        else:
            move = Movement.RIGHT 
    else:
        if snail_x_pos < 765:
            snail_x_pos+=10
        else:
            move = Movement.LEFT
    
    
    screen.blit(snail_surface, (snail_x_pos, snail_y_pos))

    

    # creating text


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()
