import pygame
#global gravity

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
gravity = True

# Player movement
class Player:
    def __init__(self, x_player, y_player, width, height):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.grav_y = 0
        self.on_ground = False
    def input(self):
        global gravity
        global keys
        keys = pygame.key.get_pressed()      
        if keys[pygame.K_LEFT]:
            self.rect.x -= 6  # Decrease x-coordinate to move left
        if keys[pygame.K_RIGHT]:
            self.rect.x += 6  # Increase x-coordinate to move right
        if keys[pygame.K_UP]:
            self.rect.y -= 12
            #self.jump()
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_SPACE] and self.on_ground == True:
            l = 0 
            for i in range (40):
              self.grav_y = -l
              l = l + 2.5
            self.rect.y += self.grav_y
            #print('space') 

player1 = Player(400, 100, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(screen, (255, 0, 0), player1.rect)  # Draw the player

    player1.input()# Handle player input 
    player1.coll_g()

    #pygame.draw.line(screen,(255,0,255),(200,300),(400,300))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
