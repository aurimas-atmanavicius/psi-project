print("Sveiki komanda!")

import pygame
pygame.init()


screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Sveiki komanda")
screen = pygame.display.set_mode((screen_width, screen_height))


# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

# Initial background color
background_color = (0, 0, 0)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Example: Change color when a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Press 'R' to change to red
                background_color = (255, 0, 0)
            elif event.key == pygame.K_g:  # Press 'G' to change to green
                background_color = (0, 255, 0)
            elif event.key == pygame.K_b:  # Press 'B' to change to blue
                background_color = (0, 0, 255)

    # Clear the screen with the current background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
exit()
