#Ignore the carried over comments, this is the framework for every level u will make
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
# Clock and Framerate
clock = pygame.time.Clock()
#All the player stuff
# class Player:
#     def __init__(self, x_player, y_player, width, height, lives):
#         self.rect = pygame.Rect(x_player, y_player, width, height)
#         self.lives = 3
#         self.y_velocity = 0
#         self.on_ground = False
#         self.alive = True
    
#     def move(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] or keys[pygame.K_a] :
#             self.rect.x -= 8
#         if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#             self.rect.x += 8
#         if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:  # Jump if on the ground
#             self.y_velocity = -15
#             self.on_ground = False
#         #if keys[pygame.K_UP]:
#          #   self.rect.y -= 8
#         #if keys[pygame.K_DOWN]:
#         #    self.rect.y += 8
#         if keys[pygame.K_r]:
#             self.rect.x = 400
#             self.rect.y = 300
#         if self.rect.x < 0:
#             self.rect.x = 0
#         if self.rect.x >= 800:
#             self.rect.x = 800

#     def apply_gravity(self):
#         if self.y_velocity< 40:
#             self.y_velocity += 1  # Gravity force
#             self.rect.y += self.y_velocity 
#         #if self.y_velocity > 40:
#         #    self.y_velocity = 0          

#     def takedam(self,opps):
#             if self.rect.colliderect(opps.rect):             
#                 self.lives -= 1
#                  #Its supposed to teleport you to the start of the level when u get hit.
#                 self.starting_pos(0,500)
    
#     def starting_pos(self,startx,starty):
#         #The starting position of each level that the player will be teleported to when they die
#         self.rect.x = startx
#         self.rect.y = starty

#     def draw(self):
#         pygame.draw.rect(screen, (0, 0, 255), self.rect) #Blue

#     def handle_collisions(self, platforms):
#         self.on_ground = False
#         for platform in platforms:
#             if self.rect.colliderect(platform.collider) and self.y_velocity > 0:
#                 self.rect.bottom = platform.collider.top
#                 self.y_velocity = 0
#                 self.on_ground = True
#All the opps ennit
class Player:
    def __init__(self, x_player, y_player, width, height, lives):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.lives = lives
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
                print(self.lives)
    
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
#wow
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
#The end of the level
class Winbox(Platform):
    def winplay(self, player):
        if self.rect.colliderect(player.rect):
            print("Level Complete")
            #screen.fill("aqua")
            level_results(player)

player = Player(0, 500, 25, 25,3)

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
        
        #Draw enemies
        for enemy in enemies:
            enemy.draw()

        # Player movement and physics
        player.move()
        player.apply_gravity()
        player.handle_collisions(platforms)

        # Draw player
        player.draw()

        #Enemy movement
        for enemy in enemies:
            enemy.movement()
            enemy.attack(player)

        # Update the display
        pygame.display.update()
        clock.tick(60)
