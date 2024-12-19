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

class Player:
    def __init__(self, x_player, y_player, width, height):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.colour = (0, 0, 255)
        #self.startposx = startposx
        #self.startposy = startposy
        self.xvel = 8
        self.yvel = 8
        self.dvel = 20
    def draw(self):
        pygame.draw.rect(screen,self.colour,self.rect)

    def movegrav(self,position):
        gravity = True
        #double_j = False
        while gravity:
            self.rect.y += 3.5
            if self.rect.collidepoint(position):
                self.rect.y_player = position + 1
                return True
        return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.xvel  # Decrease x-coordinate to move left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.xvel  # Increase x-coordinate to move right
        if keys[pygame.K_UP]:  #allow jumps, one of platform and the other in the air
            self.rect.y -= self.yvel  # Move the player up
        #if keys[pygame.K_DOWN]:
         #   self.rect.y += 5
        
player = Player(0,500,25,25)
class Platform:
    def __init__(self, x_plat, y_plat, width, height):
        self.rect = pygame.Rect(x_plat, y_plat, width, height)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
plat1 = Platform(0,600,100,100) 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    plat1.draw()  # Draw the platform
    pygame.draw.rect(screen, (0, 0, 255), player.rect)  # Draw the player

    player.movegrav(plat1)
        
    pygame.display.update()
    clock.tick(60)  
