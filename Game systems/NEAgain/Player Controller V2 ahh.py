import pygame
import sys
from sys import exit

pygame.init()
# Window Parameters and Name
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slipstream")
# Clock and Framerate
clock = pygame.time.Clock()

class Player:
    def __init__(self, x_player, y_player, width, height):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.xvel = 8
        self.yvel = 8
        self.gravity_force = 3.5
        self.is_jumping = False
        self.jump_force = 10
        self.jump_count = 10  # Used to control jump height and double jump

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.xvel  # Decrease x-coordinate to move left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.xvel  # Increase x-coordinate to move right
        if keys[pygame.K_UP]:
            if not self.is_jumping:
                self.is_jumping = True
                self.jump_count = 10  # Reset jump count for a new jump

    def apply_gravity(self, platforms):
        if self.is_jumping:
            # Apply jump force
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10
        else:
            # Apply gravity
            self.rect.y += self.gravity_force

        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and not self.is_jumping:
                self.rect.y = platform.rect.top - self.rect.height  # Place the player on top of the platform

player = Player(0, 500, 25, 25)

class Platform:
    def __init__(self, x_plat, y_plat, width, height):
        self.rect = pygame.Rect(x_plat, y_plat, width, height)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

plat1 = Platform(0, 550, 800, 50)# Adjusted platform size to fill bottom of the screen
plat2 = Platform(150, 500, 100, 50)
plat3 = Platform(300, 450, 100, 50)
plat4 = Platform(450, 400, 100, 50)
plat5 = Platform(600, 350, 100, 50)
plats = [plat1,plat2,plat3,plat4,plat5]
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # Clear screen before drawing

    for plat in plats:
        plat.draw()

    #plat1.draw()  # Draw the platform
    player.draw()  # Draw the player

    player.move()  # Handle player movement
    for plat in plats:
        player.apply_gravity([plat])
    #player.apply_gravity([plat1])# Apply gravity and handle collisions

    pygame.display.update()
    clock.tick(60)
