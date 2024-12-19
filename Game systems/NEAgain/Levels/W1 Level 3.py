#The Void is introduced as a way to die lol
import pygame
import sys
from sys import exit
import random
pygame.init()
# Window Parameters and Name
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slipstream")
# Clock and Framerate
clock = pygame.time.Clock()

#Image stuff
result_s = pygame.image.load('Game systems/NEAgain/TheTrueNEAgents/result_screen_b.png').convert()
result_s = pygame.transform.scale(result_s,(width,height))
game_o = pygame.image.load('Slipsteam_Final/Assests/GOv1.png').convert()
game_o = pygame.transform.scale(game_o,(width,height))
#Actual back button time lol
backbut = pygame.image.load('Game systems/NEAgain/TheTrueNEAgents/Back_but.png').convert()
gomenu = pygame.image.load('Slipsteam_Final/Assests/gomenu_but.png').convert()
#Font stuff
#Test Font object 
test_font = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf", 75)
test_mont = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf",75)

#The text that will be displayed
name_i = ""
name_s = ""
#Creating the text itself the text is whatever is in self.name_i and the colour is white
name = test_font.render("L i v e s: {name_i}",True,"white")
rice = test_mont.render("S c o r e: {name_s}",True,"white")

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

def level_results(player):
    while True:
        #Fills the screen and sets the background
        screen.fill("black")
        screen.blit(result_s,(0,0))
        #screen.blit(backbut,(275,475))
        
        #Gets the mouse positions so we can check for buttons later
        menu_mouse_pos = pygame.mouse.get_pos()

        #Creating the buttons that will go on the main menu by using the button class
        #back_button = Button_I(backbut,275,475)
        back_button = Button_I(backbut,390,520)
            
        back_button.update()

        name = test_font.render(f"L i v e s.  {player.recent_lives}",True,"white")
        rice = test_mont.render(f"S c o r e.   {player.recent_score}",True,"white")
            
        screen.blit(name, (10, 200))
        screen.blit(rice,(10, 300))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(menu_mouse_pos):
                    print("button")
        
             # Draw the score to the screen

def game_over():
    while True:
        #Fills the screen and sets the background
        screen.fill("black")
        screen.blit(game_o,(0,0))
        #screen.blit(backbut,(275,475))
        
        #Gets the mouse positions so we can check for buttons later
        menu_mouse_pos = pygame.mouse.get_pos()

        #Creating the buttons that will go on the main menu by using the button class
        #back_button = Button_I(backbut,275,475)
        gomenu_butt = Button_I(gomenu,390,520)
            
        gomenu_butt.update()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gomenu_butt.checkForInput(menu_mouse_pos):
                    print("button")
        
    
#All the player stuff
class Player:
    def __init__(self, x_player, y_player, width, height, lives):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.lives = 3
        self.y_velocity = 0
        self.on_ground = False
        self.alive = True
        self.score = 0
        self.recent_score = 0
        self.recent_lives = 0 
    
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
            self.rect.x = 0
            self.rect.y = 500
            self.y_velocity = 0
            self.on_ground = False
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x >= 800:
            self.rect.x = 800
        
        if self.rect.y > height:
            self.lives -= 1
                 #Its supposed to teleport you to the start of the level when u get hit.
            self.starting_pos(0,500)
            print(self.lives)

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
    
    def save_values(self):
        self.recent_lives = self.lives
        self.recent_score = self.score

    def save_values_d(self):
        global name_i
        global name_s
        name_i = self.recent_lives
        name_s = self.recent_score

    def over_game(self):
        if self.lives < 0:
            game_over()
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
class Winbox(Platform):
    def winplay(self, player):
        if self.rect.colliderect(player.rect):
            print("Level Complete")
            #screen.fill("aqua")
            level_results(player)

player = Player(0, 500, 25, 25,3)
winbox = Winbox(50,150, 30, 30)
#Platforms
plat1 = Platform(0, 550,75, 50)
plat2 = Platform(200, 450, 75, 50)
plat3 = Platform(0, 380, 75, 50)
plat4 = Platform(250, 320, 75, 50)
plat5 = Platform(450,400,75,50)
plat6 = Platform(600,500,75,50)
plat7  = Platform(600,300,75,50)
plat8  = Platform(700,175,75,50)
plat9  = Platform(500,100,75,50)
plat10 = Platform(300,65,75,50)
plat11 = Platform(90,210,2.5,2.5)
platforms = [plat1,plat2,plat3,plat4,plat5,plat6,plat7,plat8,plat9,plat10,plat11]

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
        player.save_values()
        player.save_values_d()
        player.over_game()

        # Draw player
        player.draw()

        # Update the display
        pygame.display.update()
        clock.tick(60)