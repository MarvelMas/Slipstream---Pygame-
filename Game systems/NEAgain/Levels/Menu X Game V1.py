import pygame
import sys
from sys import exit

pygame.init()
#Window Parametres and Name
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Slipstream")
#Clock and Framerate
clock = pygame.time.Clock()
#Assests
#Image stuff
result_s = pygame.image.load('Game systems/NEAgain/TheTrueNEAgents/result_screen_b.png').convert()
result_s = pygame.transform.scale(result_s,(width,height))
game_o = pygame.image.load('Slipsteam_Final/Assests/GOv1.png').convert()
game_o = pygame.transform.scale(game_o,(width,height))
levels_s = pygame.image.load('Slipsteam_Final/Assests/level_sel_bg.png').convert()
levels_s = pygame.transform.scale(levels_s,(width,height))
#Actual back button time lol
backbut = pygame.image.load('Game systems/NEAgain/TheTrueNEAgents/Back_but.png').convert()
gomenu = pygame.image.load('Slipsteam_Final/Assests/gomenu_but.png').convert()
barrow_but = pygame.image.load('Slipsteam_Final/Assests/barrow_but.png').convert()
#Level Select Button
W1_level1 = pygame.image.load('Slipsteam_Final/Assests/W1_L1_LSold.png').convert()
W1_level2 = pygame.image.load('Slipsteam_Final/Assests/W1_L2_LSold.png').convert()
W1_level3 = pygame.image.load('Slipsteam_Final/Assests/W1_L3_LSold.png').convert()
W1_level4 = pygame.image.load('Slipsteam_Final/Assests/W1_L4_LSold.png').convert()
W1_level5 = pygame.image.load('Slipsteam_Final/Assests/W1_L5_LSold.png').convert()
W1_level6 = pygame.image.load('Slipsteam_Final/Assests/W1_L6_LSold.png').convert()
#Font stuff
#Test Font object 
test_font = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf", 75)
test_mont = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf",75)
main_font = pygame.font.Font(None, 50)
#The text that will be displayed
name_i = ""
name_s = ""
#Creating the text itself the text is whatever is in self.name_i and the colour is white
name = test_font.render("L i v e s: {name_i}",True,"white")
rice = test_mont.render("S c o r e: {name_s}",True,"white")
#Image surface
credits_z = pygame.image.load('Game systems/NEAgain/NEAgents To Be Used.png').convert()
credits_z = pygame.transform.scale(credits_z,(width,height))

#All of the game stuff
#The Player program
class Player:
    def __init__(self, x_player, y_player, width, height, lives, startx, starty):
        self.rect = pygame.Rect(x_player, y_player, width, height)
        self.lives = lives
        self.y_velocity = 0
        self.on_ground = False
        self.alive = True
        self.score = 0
        self.recent_score = 0
        self.recent_lives = 0
        self.startx = startx
        self.starty = starty 
        self.deaths = 0    

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a] :
            self.rect.x -= 7
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 7
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:  # Jump if on the ground
            self.y_velocity = -16.5
            self.on_ground = False
        #if keys[pygame.K_UP]:
         #   self.rect.y -= 8
        #if keys[pygame.K_DOWN]:
        #    self.rect.y += 8
        if keys[pygame.K_r]:
            self.rect.x = self.startx
            self.rect.y = self.starty
            self.y_velocity = 0
            self.on_ground = False
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x >= 800:
            self.rect.x = 800
        
        if self.rect.y > height:
            self.lives -= 1
            self.deaths += 1
                 #Its supposed to teleport you to the start of the level when u get hit.
            self.starting_pos(self.startx,self.starty)
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
                self.starting_pos(self.startx,self.starty)
                print(self.lives)
    
    def takedam_deathless(self,opps):
        if self.rect.colliderect(opps.rect):             
                self.deaths += 1
                 #Its supposed to teleport you to the start of the level when u get hit.
                self.starting_pos(self.startx,self.starty)
                print(self.deaths)
    
    def starting_pos(self,startx,starty):
        #The starting position of each level that the player will be teleported to when they die
        self.rect.x = startx
        self.rect.y = starty

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), self.rect) #Blue

    def handle_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect)and self.y_velocity >= 0:
                self.rect.bottom = platform.rect.top
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
        if self.name == "Bulleta":
             self.damage = 1
             self.visual = (255,0,255)
        if self.name == "Bully":
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
        if self.name == "Bulleta":
             self.rect.x += 10
             if self.rect.x > 850:
                    self.reset_position(self.start_x,self.start_y)
        if self.name == "Bully":
            self.rect.y += 10
            if self.rect.y > 650:
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
        self.collider = pygame.Rect((x_plat), (y_plat), width, 4)

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
            #screen.fill("aqua")
            level_results(player)
#The Button Class
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
#Results Screen
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
                    main_menu()
#Game Over Screen        
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
                    main_menu()
#The Coins for the Shop system
class Coins:
    def __init__(self,name,x_coin, y_coin, width, height):
        self.rect = pygame.Rect(x_coin, y_coin, width, height)
        self.name = name
        self.value = 0
        self.visual = (255, 255, 255)
        self.set_attributes(name)
        self.hide_x = -100
        self.hide_y = -100

    def set_attributes(self,name):
          if name == "g_coin":
            self.value = 1
            self.visual = (255,191,0)
          elif name == "topaz":
            self.value = 5
            self.visual = (255,200,124)
          elif name == "amath":
            self.value = 10
            self.visual =(153, 102, 204)
          elif name == "diamond":
            self.value = 50
            self.visual =(185,242,255)
    
    def collection(self,player):
        if self.rect.colliderect(player.rect):
            player.coin_collect(self)
            self.rect.x = self.hide_x  # Hide the coin
            self.rect.y = self.hide_y

    def draw_coin(self): pygame.draw.rect(screen, self.visual, self.rect)

#The First World
def W1_FirstJumps_1():
    player = Player(0, 500, 25, 25,3,0,500)
    winbox = Winbox(10, 10, 30, 30)
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
        player.save_values()
        player.save_values_d()
        player.over_game()

        # Draw player
        player.draw()

        # Update the display
        pygame.display.update()
        clock.tick(60)

def W1_MoreJumps_2():
    player = Player(0, 500, 25, 25,3,0,500)
    winbox = Winbox(750, 10, 30, 30)
    #Level Elements
    ## Platforms
    plat1 = Platform(0, 550, 850, 50)
    plat2 = Platform(200, 450, 75, 50)
    plat4 = Platform(250, 310, 75, 50)
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

def W1_TrbelTrial_3():
    player = Player(0, 500, 25, 25,3,0,500)
    #Level Goal
    winbox = Winbox(10, 150, 30, 30)
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

def W1_CuatroConundrum_4():
    player = Player(12, 500, 25, 25, 15,12,500)
    #The platform placement list
    plat1 = Platform(10, 550, 100, 50)
    plat2 = Platform(150,430,75,50)
    plat3 = Platform(300,305,75,50)
    plat4 = Platform(500,355,75,50)
    plat5 = Platform(600,255,75,50)
    plat6 = Platform(310,500,75,50)
    plat7 = Platform(700,75,100,50)
    plat8 = Platform(350,500,75,50)
    plat9 = Platform(425,115,75,50)
    platforms = [plat1,plat2,plat3,plat4,plat5,plat6,plat7,plat8,plat9]

    #(self,name, x_op, y_op, width, height, start_x, start_y)
    #Enemy placement list
    enemy1 = Opps("Bullet", 150, 150, 35, 35,801,150)
    enemy2 = Opps("Bulleta", 300, 300, 35, 35,-50,300)
    enemy3 = Opps("Bullet", 801, 450, 35, 35,801,450)
    enemies = [enemy1,enemy2,enemy3]

    #da win box
    winbox = Winbox(730, 40, 30, 30)

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
            player.save_values()
            player.save_values_d()
            player.over_game()
            
            # Draw player
            player.draw()
            
            #Draw the Winbox
            winbox.draw_wb()
            winbox.winplay(player)

            #Enemy movement
            for enemy in enemies:
                enemy.movement()
                enemy.attack(player)

            # Update the display
            pygame.display.update()
            clock.tick(60)

def W1_EnumEvasion_5():
    player = Player(0, 500, 25, 25,3,15,500)
    #The platform placement list
    plat1 = Platform(1, 550, 100, 50)
    plat2 = Platform(120,450,100,50)
    plat3 = Platform(240,320,100,50)
    plat4 = Platform(380,210,100,50)
    plat5 = Platform(575,90,100,50)
    platforms = [plat1,plat2,plat3,plat4,plat5]

    #(self,name, x_op, y_op, width, height, start_x, start_y)
    #Enemy placement list
    enemy1 = Opps("Bully",130,-50,35,35,130,-50)
    enemy2 = Opps("Bully",270,-50,35,35,270,-50)
    enemy3 = Opps("Bully",420,-50,35,35,420,-50)
    enemy4 = Opps("Bully",560,-50,35,35,560,-50)
    enemies = [enemy1,enemy2,enemy3,enemy4]

    #da win box
    winbox = Winbox(730, 40, 30, 30)

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
        player.save_values()
        player.save_values_d()
        player.over_game()
            
        # Draw player
        player.draw()
            
        #Draw the Winbox
        winbox.draw_wb()
        winbox.winplay(player)

        #Enemy movement
        for enemy in enemies:
            enemy.movement()
            enemy.attack(player)

        # Update the display
        pygame.display.update()
        clock.tick(60)

def W1_SechesSlaugher_6():
    player = Player(0, 500, 25, 25,3,15,500)
    #The platform placement list
    plat1 = Platform(1, 550, 100, 50)
    plat2 = Platform(270,450,100,50)
    plat3 = Platform(130,320,75,50)
    plat4 = Platform(375,210,100,50)
    plat5 = Platform(575,90,100,50)
    platforms = [plat1,plat2,plat3,plat4,plat5]#,plat3,plat4,plat5]

    #(self,name, x_op, y_op, width, height, start_x, start_y)
    #Enemy placement list
    #Vertical foes
    enemy1 = Opps("Bully",130,-50,35,35,130,-50)
    enemy2 = Opps("Bully",270,-50,35,35,270,-50)
    enemy3 = Opps("Bully",420,-50,35,35,420,-50)
    enemy4 = Opps("Bully",560,-50,35,35,560,-50)
    #Horizontal foes
    enemy5 = Opps("Bullet", 150, 150, 35, 35,801,150)
    enemy6 = Opps("Bulleta", 300, 300, 35, 35,-50,300)
    enemy7 = Opps("Bullet", 801, 450, 35, 35,801,450)
    enemies = [enemy1,enemy2,enemy3,enemy5,enemy6]

    #da win box
    winbox = Winbox(730, 550, 30, 30)

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
            
            #Draw the Winbox
            winbox.draw_wb()
            winbox.winplay(player)

            #Enemy movement
            for enemy in enemies:
                enemy.movement()
                enemy.attack(player)

            # Update the display
            pygame.display.update()
            clock.tick(60)

def WAlphaL1(): 
    #Level 1 Alpha - WALL
    player = Player(0, 500, 25, 25,61,0,500)
    #The platform placement list
    plat1 = Platform(0, 550, 850, 50)
    plat2 = Platform(100, 450, 150, 50)
    plat3 = Platform(300, 350, 150, 50)
    plat4 = Platform(550, 250, 150, 50)
    plat5 = Platform(305, 165, 70, 50)
    plat6 = Platform(0,50, 200, 50)
    platforms = [plat1,plat2,plat3,plat4,plat5,plat6]

    #The enemy placement list
    enemy1 = Opps("Bullet", 100, 100, 35, 35,801,50)
    enemy2 = Opps("Bullet", 100, 100, 35, 35,801,100)
    enemy3 = Opps("Bullet", 100, 100, 35, 35,801,150)
    enemy4 = Opps("Bullet", 100, 100, 35, 35,801,400)
    enemy5 = Opps("Bullet", 100, 100, 35, 35,801,450)
    enemy6 = Opps("Bullet", 100, 100, 35, 35,801,500)

    enemies = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6]


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
        for enemy in enemies:
            enemy.draw()

        # Player movement and physics
        player.move()
        player.apply_gravity()
        player.handle_collisions(platforms)
        player.save_values()
        player.save_values_d()
        player.over_game()
        
        # Draw player
        player.draw()

        #Enemy movement
        for enemy in enemies:
            enemy.movement()
            enemy.attack(player)

        # Update the display
        pygame.display.update()
        clock.tick(60)

#The Menus and navigation
#Button Class that is magpied 
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
#The image buttons
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
#Creating the get_font function used to display the main menu text
def get_font(size):
    return pygame.font.Font(None, size)
#The Credits for the end of the game and credits mode
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
#Menu system
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
                    level_select()
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
#Making the level select game loop
def level_select():
    while True:
        #Fills the screen and sets the background
        screen.fill("black")
        screen.blit(levels_s,(0,0))

        #Gets the mouse positions so we can check for buttons later
        menu_mouse_pos = pygame.mouse.get_pos()

        #Creating the buttons that will go on the main menu by using the button class         
        W1_l1_button = Button_I(W1_level1,150,250)
        W1_l2_button = Button_I(W1_level2,385,250)
        W1_l3_button = Button_I(W1_level3,650,250)
        W1_l4_button = Button_I(W1_level4,150,450)
        W1_l5_button = Button_I(W1_level5,385,450)
        W1_l6_button = Button_I(W1_level6,650,450)
        back_arrow = Button_I(barrow_but,50,30)

        buttons = [W1_l1_button,W1_l2_button,W1_l3_button,W1_l4_button,W1_l5_button,W1_l6_button,back_arrow ]
        for button in buttons:
                button.update()

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
             if event.type == pygame.MOUSEBUTTONDOWN:
                if W1_l1_button.checkForInput(menu_mouse_pos):
                    W1_FirstJumps_1()  
                if W1_l2_button.checkForInput(menu_mouse_pos):
                    W1_MoreJumps_2()
                if W1_l3_button.checkForInput(menu_mouse_pos):
                    W1_TrbelTrial_3()
                if W1_l4_button.checkForInput(menu_mouse_pos):
                    W1_CuatroConundrum_4()
                if W1_l5_button.checkForInput(menu_mouse_pos):
                    W1_EnumEvasion_5()
                if W1_l6_button.checkForInput(menu_mouse_pos):
                    W1_SechesSlaugher_6()
                if back_arrow.checkForInput(menu_mouse_pos):
                    main_menu()
        
        pygame.display.update()    
                
#Button item
button = Button("clicked",400,300,100,50)
#The initiated class
main_menu()