import pygame
from sys import exit
from Source.Startup_Logo import startup_screen
from Source.Main_Menu import main_menu

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Kvizik")

    # Show startup screen
    startup_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Transition to the main menu
    main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Quit the program
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
