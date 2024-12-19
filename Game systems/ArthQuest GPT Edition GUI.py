import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arithmetic Quiz")

# Set up font
font = pygame.font.Font(None, 36)

# Global variables for tracking correct and wrong answers
correct = 0
wrong = 0

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Function to handle a single question
def handle_question(question, trueans):
    global correct, wrong
    input_text = ''
    qloop = True
    while qloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        ans = int(input_text)
                        if ans == trueans:
                            correct += 1
                        else:
                            wrong += 1
                        qloop = False
                    except ValueError:
                        input_text = ''
                        print("Please enter a valid number.")
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill((0, 0, 0))
        draw_text(question, font, (255, 255, 255), screen, screen_width // 2, screen_height // 3)
        draw_text(input_text, font, (255, 255, 255), screen, screen_width // 2, screen_height // 2)
        pygame.display.flip()

def add_quest():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    trueans = num1 + num2
    question = f"What is {num1} + {num2}?"
    handle_question(question, trueans)

def sub_quest():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    while num1 > num2:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
    trueans = num2 - num1
    question = f"What is {num2} - {num1}?"
    handle_question(question, trueans)

def multi_quest():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    trueans = num1 * num2
    question = f"What is {num1} x {num2}?"
    handle_question(question, trueans)

def div_quest():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    while num1 > num2 or num2 % num1 != 0:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
    trueans = num2 // num1
    question = f"What is {num2} ÷ {num1}?"
    handle_question(question, trueans)

def arth_quiz(name):
    global correct, wrong
    correct = 0
    wrong = 0

    addq = 0
    subq = 0
    multiq = 0
    divq = 0

    while addq + subq + multiq + divq < 12:
        current_quest = random.randint(1, 4)
        if current_quest == 1 and addq < 3:
            add_quest()
            addq += 1
        elif current_quest == 2 and subq < 3:
            sub_quest()
            subq += 1
        elif current_quest == 3 and multiq < 3:
            multi_quest()
            multiq += 1
        elif current_quest == 4 and divq < 3:
            div_quest()
            divq += 1

    print(f"The test is over! You got {correct} correct and {wrong} wrong.")

def ask_arith():
    name = input("Please type in your name: ").strip()
    ans = input("Would you like to start the quiz? Y/N ").strip().upper()
    while True:
        if ans == "Y":
            arth_quiz(name)
            ans = input("Would you like to start the quiz again? Y/N ").strip().upper()
        elif ans == "N":
            print("OK, Goodbye!")
            break
        else:
            print("Please try answering again")
            ans = input("Would you like to start the quiz? Y/N ").strip().upper()

# Start the quiz
ask_arith()
