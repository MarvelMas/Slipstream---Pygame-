#This is the second level of the game. It will feature more difficult jumps than the first but no bottomless pits. Yet :)
import pygame
import sys
from sys import exit
import random
#The plan for this code it to attempt to create a cannon of sorts that the bullet can be fired from. 
# The position it will be fire from will be a parameter hopefully
pygame.init()
# Window Parameters and Name
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slipstream")
font = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf",25)
#mouse_pos = pygame.mouse.get_pos()
# Clock and Framerate
clock = pygame.time.Clock()
#Time Stuff
start_button = pygame.Rect(200,300,75,75)
lap_button = pygame.Rect(600,300,75,75)
stop_button = pygame.Rect(400,300,75,75)

class Timer:
    def __init__(self,duration):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.start_time_stop = 0
        self.final_time = 0
        self.current_time = pygame.time.get_ticks()

    # def activ(self):
    #     self.active = True
    #     self.start_time = pygame.time.get_ticks()
    
    # def deactiv(self):
    #     self.active = False
    #     self.start_time = 0
    
    # def update(self):
    #     if self.active:
    #         current_time = pygame.time.get_ticks()
    #         if current_time - self.start_time >= self.duration:
    #             self.deactiv()

    def start_stopwatch(self):
        self.start_time_stop = pygame.time.get_ticks()
        print("Stopwatch Start")
        print(self.start_time_stop)


    def stop_stopwatch(self):
        print(self.current_time)
        print(type(self.start_time_stop))
        self.stop_time = pygame.time.get_ticks()
        print("################")
        print(self.start_time_stop, self.stop_time)
        print("##")
        
        self.final_time = (self.stop_time-self.start_time_stop)/1000
        print("Stopwatch stop")
        print(self.final_time)

test_timer = Timer(1000)
# test_timer.activ()
test_stop = Timer(909)
level2_time = Timer(0)
#All the player stuff
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
        pygame.draw.rect(screen, (0, 255, 0), self.collider)
player = Player(0, 500, 25, 25,3)

def MoreJumps():
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

            #Start timer
            level2_time.start_stopwatch
            
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

#MoreJumps()

#Current time is from when run is pressed
#Start time is when the level is selected
#Start time = current time done to make sure that you remeber when the level was started
#Start time is the start of the level select
#final time = current time - start time /1000 done to get seconds
#https://www.youtube.com/watch?v=7H6_fcRZLJY&ab_channel=Atlas




# #while True:
#     mouse_pos = pygame.mouse.get_pos()
#     for event in pygame.event.get():
#         pygame.time.get_ticks()
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
        
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             currenttime = pygame.time.get_ticks()
#             if start_button.collidepoint(mouse_pos):
#                 print("Start Button press")
#                 # starttime = currenttime
#                 # print(starttime)

#                 test_timer.start_stopwatch()
                

#             if lap_button.collidepoint(mouse_pos):
#                 print("Lap Button press")
            
#             if stop_button.collidepoint(mouse_pos):
#                 print("Stop Button press")      
#                 # finaltime= (currenttime-starttime)/1000
#                 # print(finaltime)
#                 test_timer.stop_stopwatch()  

   
# #    test_timer.update() 
   
#     # if test_timer.active:
#     #    text_surf = font.render('1 second passed',False,'white')
#     #    screen.blit(text_surf,(0,0))
   
#     pygame.draw.rect(screen, ("green"), start_button)
#     pygame.draw.rect(screen, ("blue"), lap_button)
#     pygame.draw.rect(screen, ("red"), stop_button)
#     pygame.display.update()
