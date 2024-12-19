import pygame, sys
import os
import random
pygame.init()
pygame.font.init()

score = 0
score_increment = 10
# Set up the font object
font = pygame.font.Font(None, 36)


# Set up the window
screen = pygame.display.set_mode((750, 450))

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player character
player = pygame.Rect(100, 200, 50, 50)

# Set up the obstacle
obstacle = pygame.Rect(400, 200, 50, 50)  # Adjusted position for better initial spacing

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of all keyboard buttons
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 8
    if keys[pygame.K_RIGHT]:
        player.x += 8
    if keys[pygame.K_UP]:
        player.y -= 8
    if keys[pygame.K_DOWN]:
        player.y += 8

    # Update the game state
    if player.colliderect(obstacle):
      score += score_increment
      obstacle.x = random.randint(50,700)
      obstacle.y = random.randint(50,400)
    # Check for collision
    if player.colliderect(obstacle): pass
        #print("Collision detected!")

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), obstacle)

    # Draw the score to the screen
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()

class Coins:
    def __init__(self,name,value,visual,x_coin, y_coin, width, height):
        self.rect = pygame.Rect(x_player, y_player, width, height)

        self.value = value
        self.visual = visual
##    def cost(self,value,name):
##        if name == g_coin:
##            self.value = 1
##        elif name == topaz:
##            self.value = 5
##        elif name == amath:
##            self.value = 10
##        elif name == diamond:
##            self.value = 50
##    def visual(self,visual,name):
##        if name == g_coin:
##            self.visual = (255,191,0)
##        elif name == topaz:
##            self.visual = (255,200,124)
##        elif name == amath:
##            self.visual =(153, 102, 204)
##        elif name == diamond:
##            self.visual =(185,242,255)
    def set_attributes(self,value,visual,name):
          if name == g_coin:
            self.value = 1
            self.visual = (255,191,0)
          elif name == topaz:
            self.value = 5
            self.visual = (255,200,124)
          elif name == amath:
            self.value = 10
            self.visual =(153, 102, 204)
          elif name == diamond:
            self.value = 50
            self.visual =(185,242,255)

coin1 = Coin("g_coin", 100, 100, 20, 20)
coin2 = Coin("topaz", 150, 150, 20, 20)
coin3 = Coin("amath", 200, 200, 20, 20)
coin4 = Coin("diamond", 250, 250, 20, 20)





























                 
