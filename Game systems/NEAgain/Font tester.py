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

#Test Font object 
test_font = pygame.font.Font(None, 100)
test_mont = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf",75)

#The text that will be displayed
name_i = "L i v e s"
name_s = "S c o r e"
#Creating the text itself the text is whatever is in self.name_i and the colour is white
name = test_font.render(name_i,True,"white")
rice = test_mont.render(name_s,True,"white")
#This updates the screen to show the button    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(name,(400,300))
    screen.blit(rice,(225.5,100))
    pygame.display.flip()
    clock.tick(60)

#score = 0
#score_increment = 10
# Set up the font object
#font = pygame.font.Font(None, 36)
#score_text = font.render(f'Score: {score}', True, (255, 255, 255))
#screen.blit(score_text, (10, 10))
