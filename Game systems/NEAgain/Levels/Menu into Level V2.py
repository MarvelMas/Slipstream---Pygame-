import pygame
import sys
from sys import exit
import random
from Comp_Levels import *
#This is the testing for importing levels
#Hopefully trying to connect to the existing variables.
pygame.init()
#Window Parametres and Name
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Slipstream")
#Clock and Framerate
clock = pygame.time.Clock()
#Font object (cant believe i forgot this lol)
main_font = pygame.font.Font(None, 50)
#A variable with the mouse_position
mouse_pos = pygame.mouse.get_pos()
#Main menu class, sets up backgroud in v1 does buttons as well

credits_z = pygame.image.load('Game systems/NEAgain/NEAgents To Be Used.png').convert()
credits_z = pygame.transform.scale(credits_z,(width,height))

#Actual back button time lol
backbut = pygame.image.load('Game systems/NEAgain/TheTrueNEAgents/Back_but.png').convert()

#Button Class that is magpied 
class Button():
    def __init__(self, name_i, x_pos, y_pos, width, height):
        #self.rect_b = pygame.Rect(x_pos, y_pos, width, height)
        #The text that will be displayed
        self.name_i = name_i
        #Creating the text itself the text is whatever is in self.name_i and the colour is white
        self.name = main_font.render(self.name_i,True,"black")
        #This creates a rect that the text can actually be put and displayed on
        self.name_rect = self.name.get_rect(center = (x_pos, y_pos))
    #This updates the screen to show the button    
    def update(self):
        screen.blit(self.name, self.name_rect)
    #This checks if the mouse has interacted with the button
    def checkForInput(self,position):
#        if position[0] in range (self.name_rect.left,self.name_rect.right) and position[1] in range(self.name_rect.top,self.name_rect.bottom):
        if self.name_rect.collidepoint(position):
            print("Button press")
            return True
        return False
