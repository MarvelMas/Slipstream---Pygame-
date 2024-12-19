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
        self.y_velocity = 0
        self.on_ground = False

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
        if self.y_velocity > 50:
            self.y_velocity = 0

    def handle_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.collider) and self.y_velocity > 0:
                self.rect.bottom = platform.collider.top
                self.y_velocity = 0
                self.on_ground = True

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

class Platform:
    def __init__(self, x_plat, y_plat, width, height):
        self.rect = pygame.Rect(x_plat, y_plat, width, height)
        # Define an invisible line at the top of the platform
        self.collider = pygame.Rect(x_plat, y_plat, width, 1)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        # Optional: Draw the collider line for debugging purposes
        pygame.draw.rect(screen, (0, 255, 0), self.collider)

class Winbox(Platform):
    def winplay(self,player):
        if self.rect.colliderect(player.collider):
            level_complete = True

# Initialize player and platforms
player = Player(0, 500, 25, 25)

#plat1 = Platform(0, 550, 850, 50)
#plat2 = Platform(100, 450, 150, 50)
#plat3 = Platform(300, 350, 150, 50)
#plat4 = Platform(550, 250, 150, 50)
#plat5 = Platform(305, 165, 70, 50)
#plat6 = Platform(0,50, 200, 50)
#platforms = [plat1,plat2,plat3,plat4,plat5,plat6]

#Cal`s level
plat1 = Platform(0, 550, 850, 50)
plat7 = Platform(0, 375, 85, 50)
plat2 = Platform(100, 500, 15, 50)
plat3 = Platform(200, 275, 15, 50)
plat4 = Platform(300, 275, 15, 50)
plat5 = Platform(400, 200, 70, 50)
plat6 = Platform(300,75, 20, 50)
plat8 = Platform(0,25, 300, 50)
plat9 = Platform(500,50, 200, 50)
platforms = [plat1,plat2,plat3,plat4,plat5,plat6,plat7,plat8,plat9]


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

    # Player movement and physics
    player.move()
    player.apply_gravity()
    player.handle_collisions(platforms)

    # Draw player
    player.draw()

    # Update the display
    pygame.display.update()
    clock.tick(60)
