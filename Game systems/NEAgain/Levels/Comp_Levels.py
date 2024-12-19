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
#Actual back button time lol
backbut = pygame.image.load('Game systems/NEAgain/TheTrueNEAgents/Back_but.png').convert()
gomenu = pygame.image.load('Slipsteam_Final/Assests/gomenu_but.png').convert()
#Font stuff
#Test Font object 
test_font = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf", 60)
test_mont = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf",60)
test_dont = pygame.font.Font("Slipsteam_Final/Assests/PEPSI_pl.ttf",60)
#The text that will be displayed
name_i = ""
name_s = ""
#Creating the text itself the text is whatever is in self.name_i and the colour is white
name = test_font.render("L i v e s: {name_i}",True,"white")
rice = test_mont.render("S c o r e: {name_s}",True,"white")
 
#Game Classes and Variables
# class Player:
#     def __init__(self, x_player, y_player, width, height, lives):
#         self.rect = pygame.Rect(x_player, y_player, width, height)
#         self.lives = 3
#         self.y_velocity = 0
#         self.on_ground = False
#         self.alive = True
#         self.score = 0
#         self.recent_score = 0
#         self.recent_lives = 0
    
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
#             self.rect.x = 0
#             self.rect.y = 500
#             self.y_velocity = 0
#             self.on_ground = False
#         if self.rect.x < 0:
#             self.rect.x = 0
#         if self.rect.x >= 800:
#             self.rect.x = 800
#         if self.rect.y > height:
#             self.lives -= 1
#                  #Its supposed to teleport you to the start of the level when u get hit.
#             self.starting_pos(0,500)
#             print(self.lives)
#             if self.lives < -1:
#                 print("Game Over!")

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
#             if self.rect.y > height:
#                 self.lives -= 1
#                 #Take damage if u fall into the void
#                 player.starting_pos(0,500)
    
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

#     def level_end_finish(self):
#         if self.lives < -1:
#             pass
    
#     def save_values(self):
#         self.recent_lives = self.lives
#         self.recent_score = self.score
#Soptwatch stuff
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
        self.recent_time = 0
        self.best_time_L1 = 0
        self.best_time_L2 = 0
        self.best_time_L3 = 0
        self.best_time_L4 = 0
        self.best_time_L5 = 0
        self.best_time_L6 = 0
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
            if self.rect.colliderect(platform.collider) and self.y_velocity >= 0:
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

    def save_values_time(self,recent_time_pass):
        self.recent_time = recent_time_pass
        print(recent_time_pass)

    def over_game(self):
        if self.lives < 0:
            game_over()

    def coin_collect(self,coin):
        if self.rect.colliderect(coin.rect):             
                self.score += coin.value 
                 #This should hopefully work with the coin system, its based on the opp collision work ish please
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
        self.collider = pygame.Rect(x_plat, y_plat, width, 1)

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
            Timer.stop_stopwatch
            #print(Timer.stop_stopwatch.final_time)
    def stopwatch_stop(self,player,stopwat):
        if self.rect.colliderect(player.rect):
            print("Level End")
            for watch in stopwat:
                watch.stop_stopwatch()
                print(watch.final_time)
                player.save_values_time(watch.final_time) 
    
    def stopwatch_stop_level_result(self,player,stopwat):
        if self.rect.colliderect(player.rect):
            print("Level End")
            for watch in stopwat:
                watch.stop_stopwatch()
                print(watch.final_time)
                player.save_values_time(watch.final_time)
                speed_level_results(player)
           
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
        
        #print(Timer.final_time)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(menu_mouse_pos):
                    print("button")
#Speedrunning results screen
def speed_level_results(player):
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
        tims = test_dont.render(f"T i m e. {str(player.recent_time) + "  sec"}",True,"white")
            
        screen.blit(name, (10, 200))
        screen.blit(rice,(10, 300))
        screen.blit(tims, (10, 400))

        pygame.display.update()
        
        #print(Timer.final_time)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(menu_mouse_pos):
                    print("button")
            
            
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
                    print("button")


#player = Player(0, 500, 25, 25,5)
#winbox = Winbox(10, 10, 30, 30)

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

    #Coin Placement list
    coin1 = Coins("g_coin",50,500,15,15)
    coin2 = Coins("g_coin",375,330,15,15)
    coin3 = Coins("g_coin",615,225,15,15)
    coin4 = Coins("g_coin",325,145,15,15)
    coin5 = Coins("g_coin",75,20,15,15)
    monies = [coin1,coin2,coin3,coin4,coin5]
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
        #player.coin_collect()

        # Draw player
        player.draw()

        #Coin stuff
        for penny in monies:
                penny.draw_coin()
                penny.collection(player)
                
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

    #Coins
    coin1 = Coins("g_coin",50,500,15,15)
    coin2 = Coins("g_coin",275,285,15,15)
    coin3 = Coins("g_coin",115,200,15,15)
    coin4 = Coins("g_coin",350,95,15,15)
    coin5 = Coins("g_coin",75,20,15,15)
    coin6 = Coins("g_coin",600,140,15,15)
    monies = [coin1,coin2,coin3,coin4,coin5,coin6]

    #Timer
    level2_time = Timer(0)
    stopwat =[level2_time]
    level2_time.start_stopwatch()
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
            
            #Stopwatch testing
            #level2_time.start_stopwatch()
            #print(level2_time.start_time)
            
            #for watch in stopwat:
            #    watch.start_stopwatch()
            
            #Draw the Winbox
            #winbox.stopwatch_stop(player,stopwat)
            winbox.draw_wb()
            winbox.stopwatch_stop_level_result(player,stopwat)
            #winbox.winplay(player)
            
            
            # Player movement and physics
            player.move()
            player.apply_gravity()
            player.handle_collisions(platforms)
            player.save_values()
            player.save_values_d()
            player.over_game()
            
            # Draw player
            player.draw()

            #Coin Stuff
            for penny in monies:
                penny.draw_coin()
                penny.collection(player)
            
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

    #Coins
    coin1 = Coins("g_coin",50,500,15,15)
    coin2 = Coins("g_coin",275,285,15,15)
    coin3 = Coins("g_coin",608,277,15,15)
    coin4 = Coins("g_coin",535,70,15,15)
    coin5 = Coins("g_coin",90,70,15,15)
    monies = [coin1,coin2,coin3,coin4,coin5]

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
            
            #Coin code
            for penny in monies:
                penny.draw_coin()
                penny.collection(player)


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

    #Coins
    coin1 = Coins("g_coin",50,500,15,15)
    coin2 = Coins("g_coin",275,285,15,15)
    coin3 = Coins("g_coin",608,277,15,15)
    coin4 = Coins("g_coin",607,120,15,15)
    #coin5 = Coins("g_coin",90,70,15,15)
    coin6 = Coins("g_coin",369,477,15,15)
    #Coin 6 is on the bottom 
    monies = [coin1,coin2,coin3,coin4,coin6]

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

            #Coin stuff
            for penny in monies:
                penny.draw_coin()
                penny.collection(player)            
            
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

    #Coin Placement list
    coin1 = Coins("g_coin",50,500,15,15)
    coin2 = Coins("g_coin",160,430,15,15)
    coin3 = Coins("g_coin",283,291,15,15)
    coin4 = Coins("g_coin",426,185,15,15)
    coin5 = Coins("g_coin",616,65,15,15)
    monies = [coin1,coin2,coin3,coin4,coin5]

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

        #Coin stuff
        for penny in monies:
            penny.draw_coin()
            penny.collection(player)  

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

    #Coin Placement list
    coin1 = Coins("g_coin",50,500,15,15)
    coin2 = Coins("g_coin",181,290,15,15)
    coin3 = Coins("g_coin",319,431,15,15)
    coin4 = Coins("g_coin",410,179,15,15)
    coin5 = Coins("g_coin",622,64,15,15)
    monies = [coin1,coin2,coin3,coin4,coin5]

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

            #Coin stuff
            for penny in monies:
                penny.draw_coin()
                penny.collection(player)

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

#W1_SechesSlaugher_6()
#W1_EnumEvasion_5()
#W1_CuatroConundrum_4()
#W1_TrbelTrial_3()
W1_MoreJumps_2()
#W1_FirstJumps_1()
#WAlphaL1()
