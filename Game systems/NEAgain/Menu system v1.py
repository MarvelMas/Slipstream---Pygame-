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
#Font object (cant believe i forgot this lol)
main_font = pygame.font.Font(None, 50)
#A variable with the mouse_position
mouse_pos = pygame.mouse.get_pos()
#Main menu class, sets up backgroud in v1 does buttons as well
#Ok so I'm changing this instead im doing a Menu main class with sub classes inherting everything they need to lol
#There will also be a button class since I would like to navigate using a mouse though I may try making a version that uses only keyboad as well
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
        if position[0] in range (self.name_rect.left,self.name_rect.right) and position[1] in range(self.name_rect.top,self.name_rect.bottom):
            print("Button press")



class Menu:
    def __init__(self, name, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.maintext = ""
        self.button = button
    
    def background():pass
        
#Creating the get_font function used to display the main menu text
def get_font(size):
    return pygame.font.Font(None, size)


#Creating the main menu game loop
def main_menu():
   while True:
       #Fills the screen and sets the background
       screen.fill("aqua")
       
       #Gets the mouse positions so we can check for buttons later
       menu_mouse_pos = pygame.mouse.get_pos()

       #Creates the text that will go on the menu screen
       menu_text = get_font(100).render("Slipstream",True,"black")
       menu_rect = menu_text.get_rect(center =(400,100))

       #Creating the buttons that will go on the main menu by using the button class from before
       start_button = Button("Start",400,200,100,50)

       options_button = Button("Options",400,300,100,50)

       credits_button = Button("Credits",400,400,100,50)

       quit_button = Button("Quit",400,500,100,50)
        
       #Buttons get put into list to make executing methods more efficient.
       Buttons_l = [start_button,options_button,credits_button,quit_button]                               

                                      
       screen.blit(menu_text,menu_rect)
        
       #This runs the update code for all the buttons 
       for button in Buttons_l:
            button.update()

       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkForInput(menu_mouse_pos):
                    level_select()
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if credits_button.checkForInput(menu_mouse_pos):
                    credits_game()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
            #for i in Buttons_l:
             #   button.update
                                      
       pygame.display.update()
                    
main_menu()

button = Button("clicked",400,300,100,50)

##while True:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            exit()
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            button.checkForInput(pygame.mouse.get_pos())
##
##    screen.fill("Black")
##
##    button.update()
##    #draw all our elements
##    #update everything
##    pygame.display.update()
##    clock.tick(60)         

#main_menu()
