import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FONT_NAME = "Arial"
FONT_SIZE = 36

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Create a function to display text
def display_text(text, x, y, color=WHITE, font_size=FONT_SIZE):
    font = pygame.font.Font(pygame.font.match_font(FONT_NAME), font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

input_box = ""
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                try:
                    guess = int(input_box)
                    if guess < secret_number:
                        input_box = "Higher"
                    elif guess > secret_number:
                        input_box = "Lower"
                    else:
                        input_box = "Congratulations! You guessed it!"
                except ValueError:
                    input_box = "Invalid input. Enter a number."

    # Clear the screen
    screen.fill(BLUE)

    # Draw the title and instructions
    display_text("Guess the Number (1-100)", WIDTH // 2, 100)
    display_text("Enter your guess and press ENTER", WIDTH // 2, 150)

    # Display the result or input box
    display_text(input_box, WIDTH // 2, 300, font_size=32)

    pygame.display.flip()

# Quit pygame
pygame.quit()
