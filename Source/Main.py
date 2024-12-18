import pygame
from sys import exit
import os
from Startup_Logo import startup_screen
from Main_Menu import main_menu
import json

os.environ['SDL_VIDEO_CENTERED'] = '0'

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MUSIC_VOLUME = 0

def main():
    # Initialize Pygame
    pygame.init()

    # Initialize the mixer for sound
    pygame.mixer.init()

    # Delay for half a second (500 milliseconds)
    pygame.time.delay(1000)

    # Load and play the startup sound
    pygame.mixer.music.load("../Audio/Startup.wav")  # Replace with your file path
    pygame.mixer.music.set_volume(MUSIC_VOLUME)  # Set volume (0.0 to 1.0)
    pygame.mixer.music.play()  # Play the sound

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("KviZik")

    # Show startup screen
    startup_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)


    # Load the background song
    pygame.mixer.music.load("../Audio/main_menu_loop.wav")  # Replace with your file path
    pygame.mixer.music.set_volume(MUSIC_VOLUME)  # Set the music volume (0.0 to 1.0)
    pygame.mixer.music.play(-1, fade_ms=3000)  # Loop the music with a 3-second fade-in

    # Transition to the main menu
    main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, MUSIC_VOLUME)

    # Quit the program
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
