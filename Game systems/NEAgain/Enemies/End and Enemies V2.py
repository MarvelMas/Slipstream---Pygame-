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

class Player:
    def __init__(self, x_player, y_player, width, height, lives):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.y_velocity = 0
        self.on_ground = False
        self.lives = 3
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 8
        if keys[pygame.K_RIGHT]:
            self.rect.x += 8
        if keys[pygame.K_SPACE] and self.on_ground:  # Jump if on the ground
            self.y_velocity = -15
            self.on_ground = False
        if keys[pygame.K_r]:
            self.rect.x = 550
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x >= 800:
            self.rect.x = 800           

    def apply_gravity(self):
        self.y_velocity += 1  # Gravity force
        self.rect.y += self.y_velocity

    def handle_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.collider) and self.y_velocity > 0:
                self.rect.bottom = platform.collider.top
                self.y_velocity = 0
                self.on_ground = True

    def takedam(self,opps):
            if self.rect.colliderect(opps.rect):             
                self.lives -= 1
                 #Its supposed to teleport you to the start of the level when u get hit.
                player.starting_pos(0,500)
    
    def starting_pos(self,startx,starty):
        #The starting position of each level that the player will be teleported to when they die
        self.rect.x = startx
        self.rect.y = starty


    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), self.rect) #Blue

class Platform:
    def __init__(self, x_plat, y_plat, width, height):
        self.rect = pygame.Rect(x_plat, y_plat, width, height)
        # Define an invisible line at the top of the platform
        self.collider = pygame.Rect(x_plat, y_plat, width, 1)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        # Optional: Draw the collider line for debugging purposes
        #pygame.draw.rect(screen, (0, 255, 0), self.collider)

class Winbox(Platform):
    def winplay(self,player):
        if self.rect.colliderect(player.collider):
            level_complete = True

class Opps:
    def __init__(self,name, x_op, y_op, width, height):
        self.rect = pygame.Rect(x_op, y_op, width, height)
        self.name = name
        self.damage = 0
        self.visual = (255, 255, 255)
        self.set_attributes()
        #self.collider = pygame.Rect(x_op, y_op, width,1)

    def set_attributes(self):
        if self.name == "Phantom":
            self.damage = 1
            self.visual = (210, 4, 45) #Red
        elif self.name == "Bat":
            self.damage = 1
            self.visual = (255,0,255) #Magenta

    def reset_position(self,x_op,y_op):
        #For the moving the thing
        self.rect.x = x_op
        self.rect.y = y_op

    def movement(self):
        #Enemy movement, each one has different qualities
        if self.name == "Phantom":
            self.rect.x -= 10
            if self.rect.x < -50:
                self.reset_position(700,515)
                pass
                # This works but it probably has to be redone because something tells me im gonna have issues lol
        elif self.name == "Bat":
            self.rect.y -= 5
            if self.rect.y < -50:
                self.rect.y = 460
                self.rect.x = random.randint(50, 700)
    #I'm trying to code it so when ever they collide the player loses a life
    #I think i may have made this more complex than nessesary.
    
    def attack(self, player):
        if self.rect.colliderect(player.rect):
            player.takedam(self)         

    
    def draw(self):
        pygame.draw.rect(screen,self.visual, self.rect)
#An enemy that moves left and right like a goomba
enemy1 = Opps("Phantom", 100, 100, 35, 35)
#enemy2 = Opps("Phantom_V", 150, 150, 50, 50)

# Initialize player and platforms
player = Player(0, 500, 25, 25,3)

#Removed the platforms from the screen to increase the clarity
plat1 = Platform(0, 550, 850, 50)
#plat2 = Platform(100, 450, 150, 50)
#plat3 = Platform(300, 350, 150, 50)
#plat4 = Platform(550, 250, 150, 50)
#plat5 = Platform(305, 165, 70, 50)
#plat6 = Platform(0,50, 200, 50)
platforms = [plat1]#plat2,plat3,plat4,plat5,plat6]
opps = ["Phantom"]

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
    
    #Draw enemies
    enemy1.draw()

    # Player movement and physics
    player.move()
    player.apply_gravity()
    player.handle_collisions(platforms)

    # Draw player
    player.draw()

    #Enemy movement
    enemy1.movement()
    enemy1.attack(player)

    # Update the display
    pygame.display.update()
    clock.tick(60)

