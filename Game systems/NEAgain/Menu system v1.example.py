import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors
AQUA = (0, 255, 255)       # Background color
BUTTON_COLOR = (200, 200, 200)  # Grey placeholder color
BUTTON_BORDER = (0, 0, 0)       # Black border

# Button dimensions and positions
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 75
BUTTON_MARGIN = 50

# Positions for buttons (you can adjust these positions)
button1_rect = pygame.Rect(100, 150, BUTTON_WIDTH, BUTTON_HEIGHT)
button2_rect = pygame.Rect(550, 150, BUTTON_WIDTH, BUTTON_HEIGHT)
button3_rect = pygame.Rect(100, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
button4_rect = pygame.Rect(550, 400, BUTTON_WIDTH, BUTTON_HEIGHT)

# Create the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Button Placeholder Window")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with aqua
    screen.fill(AQUA)

    # Draw button placeholders (rectangles)
    pygame.draw.rect(screen, BUTTON_COLOR, button1_rect)
    pygame.draw.rect(screen, BUTTON_BORDER, button1_rect, 2)  # Border for clarity

    pygame.draw.rect(screen, BUTTON_COLOR, button2_rect)
    pygame.draw.rect(screen, BUTTON_BORDER, button2_rect, 2)

    pygame.draw.rect(screen, BUTTON_COLOR, button3_rect)
    pygame.draw.rect(screen, BUTTON_BORDER, button3_rect, 2)

    pygame.draw.rect(screen, BUTTON_COLOR, button4_rect)
    pygame.draw.rect(screen, BUTTON_BORDER, button4_rect, 2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
