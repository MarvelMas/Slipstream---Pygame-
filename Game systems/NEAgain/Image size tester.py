#This is used to test the size of the sprites and stuff
import pygame
import sys
from sys import exit
import random

pygame.init()
#Window Parametres and Name
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Slipstream")
#Clock and Framerate
clock = pygame.time.Clock()

#Image surface
credits_z = pygame.image.load('TheTrueNEAgents/Credits Zero.png').convert()
credits_z = pygame.transform.scale(credits_z,(width,height))

#Back Button testing
basebutton = pygame.Rect(400,550, 241, 83)

#Actual back button time lol
backbut = pygame.image.load('TheTrueNEAgents/Back_but.png').convert()

#Screen Transition testing
trascreen = pygame.image.load('TheTrueNEAgents/Btarrow.png')
trascreen = pygame.transform.scale(trascreen,(width,height))
trascreen_fl = pygame.image.load('TheTrueNEAgents/BtarrowFL.png')
x = 0
y = 0

# Counter for the number of loops
loop_count = 0
max_loops = 1
moving = True

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill('black')

    # Move the arrow across the screen
    
    if moving:
        x += 5
        if x > width:
            x = -trascreen.get_width()# Reset to start just off the left side
            loop_count += 1

        # Stop moving the arrow after 3 loops
        if loop_count >= max_loops:
            moving = False

    
    screen.blit(trascreen, (x, y))
    #credits_game()
    #x = 0
    #screen.blit(credits_z,(0,0))
    #screen.blit(backbut,(275,475))
    #pygame.draw.rect(screen, (255, 255, 255), (275,475, 241, 83))
    #screen.fill('black')

    pygame.display.update()
    clock.tick()
