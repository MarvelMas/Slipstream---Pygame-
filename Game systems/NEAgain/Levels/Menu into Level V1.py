import pygame
import sys
from sys import exit
from Comp_Levels import *

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
credits_z = pygame.image.load('Game systems/NEAgain/NEAgents To Be Used.png').convert()
credits_z = pygame.transform.scale(credits_z,(width,height))

#Actual back button time lol
backbut = pygame.image.load('Game systems/NEAgain/TheTrueNEAgents/Back_but.png').convert()

#Game Classes and Variables
class Player:
    def __init__(self, x_player, y_player, width, height, lives):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.lives = 3
        self.y_velocity = 0
        self.on_ground = False
        self.alive = True
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a] :
            self.rect.x -= 8
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 8
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:  # Jump if on the ground
            self.y_velocity = -15
            self.on_ground = False
        #if keys[pygame.K_UP]:
         #   self.rect.y -= 8
        #if keys[pygame.K_DOWN]:
        #    self.rect.y += 8
        if keys[pygame.K_r]:
            self.rect.x = 400
            self.rect.y = 300
            self.y_velocity = 0
            self.on_ground = False
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x >= 800:
            self.rect.x = 800

    def apply_gravity(self):
        if self.y_velocity< 40:
            self.y_velocity += 1  # Gravity force
            self.rect.y += self.y_velocity 
        #if self.y_velocity > 40:
        #    self.y_velocity = 0          

    def takedam(self,opps):
            if self.rect.colliderect(opps.rect):             
                self.lives -= 1
                 #Its supposed to teleport you to the start of the level when u get hit.
                self.starting_pos(0,500)
            if self.rect.y > height:
                self.lives -= 1
                #Take damage if u fall into the void
                player.starting_pos(0,500)
    
    def starting_pos(self,startx,starty):
        #The starting position of each level that the player will be teleported to when they die
        self.rect.x = startx
        self.rect.y = starty

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), self.rect) #Blue

    def handle_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.collider) and self.y_velocity > 0:
                self.rect.bottom = platform.collider.top
                self.y_velocity = 0
                self.on_ground = True
#All the opps ennit
class Opps:
    def __init__(self,name, x_op, y_op, width, height, start_x, start_y):
        self.rect = pygame.Rect(x_op, y_op, width, height)
        self.name = name
        self.damage = 0
        self.visual = (255, 255, 255)
        self.set_attributes()
        self.start_x = start_x
        self.start_y = start_y
       

    def set_attributes(self):
        #if self.name == "Phantom":
         #   self.damage = 1
          #  self.visual = (210, 4, 45) #Red
        if self.name == "Bullet":
             self.damage = 1
             self.visual = (255,0,255)

    def reset_position(self,start_x, start_y):
        #For the moving the thing
        self.rect.x = start_x
        self.rect.y = start_y

    def movement(self):
        #Enemy movement, each one has different qualities
        #if self.name == "Phantom":
        #    self.rect.x -= 10
        #    if self.rect.x < -50:
        #        self.reset_position(700,515)
        #        pass
                # This works but it probably has to be redone because something tells me im gonna have issues lol
        #Enemy movement, each one has different qualities
        if self.name == "Bullet":
             self.rect.x -= 10
             if self.rect.x < -50:
                    self.reset_position(self.start_x,self.start_y)
             
    
    #I'm trying to code it so when ever they collide the player loses a life
    #I think i may have made this more complex than nessesary.
    
    def attack(self, player):
        if self.rect.colliderect(player.rect):
            player.takedam(self)         

    
    def draw(self):
        pygame.draw.rect(screen,self.visual, self.rect)
#All of the platform stuff
class Platform:
    def __init__(self, x_plat, y_plat, width, height):
        self.rect = pygame.Rect(x_plat, y_plat, width, height)
        # Define an invisible line at the top of the platform
        self.collider = pygame.Rect(x_plat, y_plat, width, 1)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        # Optional: Draw the collider line for debugging purposes
        #pygame.draw.rect(screen, (0, 255, 0), self.collider)
    def draw_wb(self): pygame.draw.rect(screen, (0, 255, 0), self.rect)
#The Win Box
class Winbox(Platform):
    def winplay(self, player):
        if self.rect.colliderect(player.rect):
            print("Level Complete")
            screen.fill("aqua")

player = Player(0, 500, 25, 25,3)
winbox = Winbox(10, 10, 30, 30)
#All of the levels (Oh boy this is not gonna go well lol)
def W1_FirstJumps():
    player = Player(0, 500, 25, 25,3)
        #The platform placement list
    plat1 = Platform(0, 550, 850, 50)
    plat2 = Platform(100, 450, 150, 40)
    plat3 = Platform(300, 350, 150, 40)
    plat4 = Platform(550, 250, 150, 40)
    plat5 = Platform(305, 165, 70, 40)
    plat6 = Platform(0,50, 200, 40)
    platforms = [plat1,plat2,plat3,plat4,plat5,plat6]

        # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Clear the screen
        screen.fill("black")

        # Draw platforms
        for platform in platforms:
                platform.draw()
            
        #Draw the Winbox
        winbox.draw_wb()
        winbox.winplay(player)
            
        # Player movement and physics
        player.move()
        player.apply_gravity()
        player.handle_collisions(platforms)

        # Draw player
        player.draw()

        # Update the display
        pygame.display.update()
        clock.tick(60)

def W1_MoreJumps():
    #Level Elements
    ## Platforms
    plat1 = Platform(0, 550, 850, 50)
    plat2 = Platform(200, 450, 75, 50)
    plat4 = Platform(250, 320, 75, 50)
    plat3 = Platform(0, 380, 75, 50)
    plat5 = Platform(0, 230, 75, 50)
    plat6 = Platform(180, 150, 75, 50)
    plat7 = Platform(380, 145, 75, 50)
    plat8 = Platform(580, 160, 75, 50)
    plat9 = Platform(730, 50, 75, 50)
    platforms = [plat1,plat2,plat3,plat4,plat5,plat6,plat7,plat8,plat9]

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear the screen
            screen.fill("black")

            # Draw platforms
            for platform in platforms:
                platform.draw()
            

            # Player movement and physics
            player.move()
            player.apply_gravity()
            player.handle_collisions(platforms)

            # Draw player
            player.draw()

            # Update the display
            pygame.display.update()
            clock.tick(60)

#Button Class that is magpied 
# 
class Button:
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

class Button_I:
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
                    main_menu()

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
                    #W1_FirstJumps_1()
                    W1_TrbelTrial_3()
                if options_button.checkForInput(menu_mouse_pos):
                    print("options()")
                if credits_button.checkForInput(menu_mouse_pos):
                    credits_game()
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

main_menu()
#credits_game()
