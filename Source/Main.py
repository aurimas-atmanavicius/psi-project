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

    # Initialize the mixer for sound
    pygame.mixer.init()

    # Delay for half a second (500 milliseconds)
    pygame.time.delay(1000)

    # Load and play the startup sound
    pygame.mixer.music.load("../Audio/Startup.wav")  # Replace with your file path
    pygame.mixer.music.set_volume(0.5)  # Set volume (0.0 to 1.0)
    pygame.mixer.music.play()  # Play the sound

    # Create screen
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
