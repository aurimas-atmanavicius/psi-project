import pygame
import random

def fade_to_color(screen, target_color, duration=500):
    """Fades the background to a target color over the specified duration (in milliseconds)."""
    clock = pygame.time.Clock()
    fade_steps = int(duration / 16)  # Approximate number of frames for smooth fade
    current_color = screen.get_at((0, 0))[:3]  # Get the current background color

    for i in range(fade_steps + 1):
        # Calculate the color step
        intermediate_color = [
            current_color[j] + (target_color[j] - current_color[j]) * i // fade_steps
            for j in range(3)
        ]
        screen.fill(intermediate_color)  # Fill the screen with the intermediate color
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

def draw_black_squares(screen, num_squares=30):
    """Draw random black squares on the screen."""
    for _ in range(num_squares):
        x = random.randint(0, screen.get_width() - 20)
        y = random.randint(0, screen.get_height() - 20)
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 10, 10))

def draw_buttons(screen, difficulties, back_button, mouse_pos):
    """Draws the buttons for difficulties and the back button."""
    button_width = 300
    button_height = 60

    # Draw difficulty buttons
    for text, y, _ in difficulties:
        button_rect = pygame.Rect((screen.get_width() - button_width) // 2, y, button_width, button_height)
        color_hover = (200, 200, 200) if button_rect.collidepoint(mouse_pos) else (150, 150, 150)
        pygame.draw.rect(screen, color_hover, button_rect, border_radius=10)
        font = pygame.font.Font(None, 40)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    # Draw back button
    pygame.draw.rect(screen, (150, 150, 150), back_button["rect"], border_radius=10)
    back_text_surface = pygame.font.Font(None, 40).render(back_button["text"], True, (0, 0, 0))
    back_text_rect = back_text_surface.get_rect(center=back_button["rect"].center)
    screen.blit(back_text_surface, back_text_rect)

def new_game_screen(screen, width, height):  # , play_button_sound, back_to_main_menu_callback):
    """Displays the New Game screen with difficulty selection and background effects."""
    # Button data
    button_width = 300
    button_height = 60
    button_spacing = 20
    button_start_y = 200

    difficulties = [
        ("Chill", button_start_y, (255, 255, 255)),  # White background
        ("Mid", button_start_y + button_height + button_spacing, (255, 255, 0)),  # Yellow background
        ("Sigma", button_start_y + 2 * (button_height + button_spacing), (255, 0, 0)),  # Red background
    ]

    back_button = {
        "text": "Back to Main Menu",
        "rect": pygame.Rect((width - button_width) // 2, height - 150, button_width, button_height),
    }

    current_bg_color = (255, 255, 255)  # Default background color
    current_difficulty = None  # Tracks the currently hovered button

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        # Check for button hover
        hovered_difficulty = None
        for text, y, color in difficulties:
            button_rect = pygame.Rect((width - button_width) // 2, y, button_width, button_height)
            if button_rect.collidepoint(mouse_pos):
                hovered_difficulty = (text, color)  # Hovered button's text and color
                break

        # Change the background if hovering over a new button
        if hovered_difficulty and hovered_difficulty != current_difficulty:
            current_difficulty = hovered_difficulty
            # play_button_sound()  # Uncomment to play sound on hover
            fade_to_color(screen, current_difficulty[1])  # Fade to the new color
            current_bg_color = current_difficulty[1]  # Update the current background color

        # Fill the screen with the current background color
        screen.fill(current_bg_color)

        # Add black squares for "Sigma"
        if current_difficulty and current_difficulty[0] == "Sigma":
            draw_black_squares(screen)

        # Draw buttons after background changes to keep them visible
        draw_buttons(screen, difficulties, back_button, mouse_pos)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left-click
                # Back button logic
                if back_button["rect"].collidepoint(mouse_pos):
                    # play_button_sound()  # Uncomment to play sound on button click
                    # back_to_main_menu_callback()  # Uncomment to go back to main menu
                    running = False

        pygame.display.flip()

    return
