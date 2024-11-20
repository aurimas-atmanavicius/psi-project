import pygame
from sys import exit

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FONT_SIZE = 30

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
HOVER_COLOR = (150, 150, 150)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, FONT_SIZE)

# Button data: (text, y-position, callback function)
def start_new_game(): print("Starting a new game...")
def continue_game(): print("Continuing the game...")
def open_settings(): print("Opening settings...")
def view_scoreboard(): print("Viewing scoreboard...")
def exit_game():
    print("Exiting game...")
    pygame.quit()
    exit()

buttons = [
    ("New Game", 300, start_new_game),
    ("Continue", 360, continue_game),
    ("Settings", 420, open_settings),
    ("Scoreboard", 480, view_scoreboard),
    ("Exit", 540, exit_game),
]

# Main menu function
def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Main Menu")
    clock = pygame.time.Clock()

    # Load the logo
    logo = pygame.image.load("../Graphics/Logo_main_screen.png")  # Replace with your logo file
    logo = pygame.transform.scale(logo, (200, 200))  # Resize logo

    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()  # Exit the game if the close button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for text, y, callback in buttons:
                    button_rect = pygame.Rect((SCREEN_WIDTH - 300) // 2, y, 300, 50)
                    if button_rect.collidepoint(mouse_pos):
                        callback()

        # Draw the logo
        screen.blit(logo, ((SCREEN_WIDTH - logo.get_width()) // 2, 50))

        # Draw buttons
        for text, y, _ in buttons:
            button_rect = pygame.Rect((SCREEN_WIDTH - 300) // 2, y, 300, 50)
            color = HOVER_COLOR if button_rect.collidepoint(mouse_pos) else GRAY
            pygame.draw.rect(screen, color, button_rect)
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=button_rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    exit()

# Run the menu directly if this file is executed
if __name__ == "__main__":
    main_menu()
