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

#Assets that will be used
#Image surface
credits_z = pygame.image.load('NEAgain/TheTrueNEAgents/Credits Zero.png').convert()
credits_z = pygame.transform.scale(credits_z,(width,height))

#Actual back button time lol
backbut = pygame.image.load('NEAgain/TheTrueNEAgents/Back_but.png').convert()

#Screen Transition testing
trascreen = pygame.image.load('TheTrueNEAgents/Btarrow.png')
trascreen = pygame.transform.scale(trascreen,(width,height))
trascreen_fl = pygame.image.load('TheTrueNEAgents/BtarrowFL.png')


# Counter for the number of loops
#loop_count = 0
#max_loops = 1
#moving = True

#Game Loop
def trans(nextscene):
        print("This")
        #Creating the variables for the arrows lol
        x = 0
        y = 0
        print("That")
        # Move the arrow across the screen
        loop_count = 0
        max_loops = 3
        moving = True
        print("Those")            

        # Clear the screen
        print("This")
        screen.fill('black')
        
        while moving:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            x += 5
            if x > width:
                x = -trascreen.get_width()# Reset to start just off the left side
                loop_count += 1
                print("Arrow schmovemenr")
                screen.blit(trascreen, (x, y))

            # Stop moving the arrow after 3 loops
            if loop_count >= max_loops:
                moving = False

        
        screen.blit(trascreen, (x, y))
        pygame.display.update()
        clock.tick(60)

        nextscene() #Calls next screen

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

###Another button class that uses images instead
##class Button_I():
##    def __init__(self, name_image, x_pos, y_pos):
##        #self.rect_b = pygame.Rect(x_pos, y_pos, width, height)
##        self.x_pos = x_pos
##        self.y_pos = y_pos
##        #The image that will be displayed
##        self.name_image = name_image
##        #Creating the rect of the image itself 
##        self.name_I = self.name_image.get_rect(center =(self.x_pos,self.y_pos))
##        #This creates a rect that the text can actually be put and displayed on
##        self.name_rect_I = self.name_I.get_rect(center = (x_pos, y_pos))
##    #This updates the screen to show the button    
##    def update(self):
##        screen.blit(self.name_I, self.name_rect_I)
##    #This checks if the mouse has interacted with the button
##    def checkForInput(self,position):
##        if position[0] in range (self.name_rect_I.left,self.name_rect.right_I) and position[1] in range(self.name_rect_I.top,self.name_rect_I.bottom):
##            #print("Button press")
##            return True
##        return False
# Button class that uses images instead

class Button_I():
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self):
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            return True
        return False

class Menu:
    def __init__(self, name, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.maintext = ""
        self.button = button
    
    def background():pass
        
#Creating the get_font function used to display the main menu text
def get_font(size):
    return pygame.font.Font(None, size)

def credits_game():
    while True:
        #Fills the screen and sets the background
        screen.fill("black")
        screen.blit(credits_z,(0,0))
        #screen.blit(backbut,(275,475))
        
        #Gets the mouse positions so we can check for buttons later
        menu_mouse_pos = pygame.mouse.get_pos()

        #Creating the buttons that will go on the main menu by using the button class
        #back_button = Button_I(backbut,275,475)
        back_button = Button_I(backbut,390,520)
            
        back_button.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(menu_mouse_pos):
                    trans(main_menu())

            pygame.display.update()

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
                    print("level_select()")
                if options_button.checkForInput(menu_mouse_pos):
                    print("options()")
                if credits_button.checkForInput(menu_mouse_pos):
                    trans(credits_game())
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
            #for i in Buttons_l:
             #   button.update
                                      
       pygame.display.update()
                    


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
#credits_game()
trans(credits_game)
