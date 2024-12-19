import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player properties
player_width = 40
player_height = 60
player_speed = 5
player_jump_speed = 15
gravity = 1

# Level platforms and obstacles
levels = [
    [ # Level 1: Beginner's Jump
        pygame.Rect(50, SCREEN_HEIGHT - 100, 100, 10),
        pygame.Rect(200, SCREEN_HEIGHT - 150, 100, 10),
        pygame.Rect(350, SCREEN_HEIGHT - 200, 100, 10),
        pygame.Rect(500, SCREEN_HEIGHT - 250, 100, 10),
        pygame.Rect(650, SCREEN_HEIGHT - 300, 100, 10)
    ],
    [ # Level 2: Rising Tides
        pygame.Rect(50, SCREEN_HEIGHT - 100, 100, 10),
        pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 10),
        pygame.Rect(250, SCREEN_HEIGHT - 300, 100, 10),
        pygame.Rect(350, SCREEN_HEIGHT - 400, 100, 10),
        pygame.Rect(450, SCREEN_HEIGHT - 500, 100, 10),
        pygame.Rect(550, SCREEN_HEIGHT - 600, 100, 10)
    ],
    [ # Level 3: Narrow Passages
        pygame.Rect(50, SCREEN_HEIGHT - 100, 50, 10),
        pygame.Rect(150, SCREEN_HEIGHT - 150, 50, 10),
        pygame.Rect(250, SCREEN_HEIGHT - 200, 50, 10),
        pygame.Rect(350, SCREEN_HEIGHT - 250, 50, 10),
        pygame.Rect(450, SCREEN_HEIGHT - 300, 50, 10),
        pygame.Rect(550, SCREEN_HEIGHT - 350, 50, 10),
        pygame.Rect(650, SCREEN_HEIGHT - 400, 50, 10)
    ],
    [ # Level 4: Moving Madness
        pygame.Rect(50, SCREEN_HEIGHT - 100, 100, 10),
        pygame.Rect(200, SCREEN_HEIGHT - 150, 100, 10),
        pygame.Rect(350, SCREEN_HEIGHT - 200, 100, 10),
        pygame.Rect(500, SCREEN_HEIGHT - 250, 100, 10),
        pygame.Rect(650, SCREEN_HEIGHT - 300, 100, 10),
        pygame.Rect(50, SCREEN_HEIGHT - 400, 100, 10)
    ],
    [ # Level 5: Final Gauntlet
        pygame.Rect(50, SCREEN_HEIGHT - 100, 100, 10),
        pygame.Rect(150, SCREEN_HEIGHT - 150, 100, 10),
        pygame.Rect(250, SCREEN_HEIGHT - 200, 100, 10),
        pygame.Rect(350, SCREEN_HEIGHT - 250, 100, 10),
        pygame.Rect(450, SCREEN_HEIGHT - 300, 100, 10),
        pygame.Rect(550, SCREEN_HEIGHT - 350, 100, 10),
        pygame.Rect(650, SCREEN_HEIGHT - 400, 100, 10),
        pygame.Rect(50, SCREEN_HEIGHT - 500, 100, 10),
        pygame.Rect(150, SCREEN_HEIGHT - 550, 100, 10),
        pygame.Rect(250, SCREEN_HEIGHT - 600, 100, 10)
    ]
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slipstream")

# Game variables
clock = pygame.time.Clock()
player_x, player_y = 50, SCREEN_HEIGHT - player_height - 10
player_velocity_y = 0
jumping = False
current_level = 0

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def draw_platforms(platforms):
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

def reset_player():
    global player_x, player_y, player_velocity_y, jumping
    player_x, player_y = 50, SCREEN_HEIGHT - player_height - 10
    player_velocity_y = 0
    jumping = False

def main():
    global player_x, player_y, player_velocity_y, jumping, current_level

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and not jumping:
            jumping = True
            player_velocity_y = -player_jump_speed

        # Apply gravity
        if jumping:
            player_velocity_y += gravity
            player_y += player_velocity_y

            # Check for collision with platforms
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            for platform in levels[current_level]:
                if check_collision(player_rect, platform):
                    jumping = False
                    player_velocity_y = 0
                    player_y = platform.y - player_height

            # Check for ground collision
            if player_y > SCREEN_HEIGHT - player_height - 10:
                player_y = SCREEN_HEIGHT - player_height - 10
                jumping = False
                player_velocity_y = 0

        # Check for level completion
        if player_x > SCREEN_WIDTH - player_width:
            current_level += 1
            if current_level >= len(levels):
                current_level = 0  # Restart from level 1
            reset_player()

        # Clear screen
        screen.fill(WHITE)

        # Draw platforms
        draw_platforms(levels[current_level])

        # Draw player
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
