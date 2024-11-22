import pygame
import sys
pygame.init()
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HIGHLIGHT_COLOR = (0, 255, 0)

# Available screen resolutions
resolutions = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]
current_resolution = (800, 600)

# Set up the window (initial resolution)
screen = pygame.display.set_mode(current_resolution)
pygame.display.set_caption("Settings in a Single Window")

# Font for text
font = pygame.font.SysFont(None, 30)

# Drop-down menu dimensions
menu_x, menu_y = 50, 50
menu_width, menu_height = 200, 30
dropdown_open = False
infoObject = pygame.display.Info()

selected_resolution_text = font.render(f"Resolution: {infoObject.current_w}x{infoObject.current_h}", True, BLACK)

# Checkbox dimensions and initial state for fullscreen toggle
checkbox_x, checkbox_y = 50, 120
checkbox_size = 30
checkbox_checked = False  # Initially unchecked

# Volume slider dimensions
slider_x, slider_y = 50, 200
slider_width = 300
slider_height = 10
slider_knob_pos = [slider_x + int(slider_width * 0.5), slider_y + slider_height // 2]
slider_value = 0.5  # Initial volume (50%)
pygame.mixer.music.set_volume(slider_value)  # Set initial volume

def draw_dropdown(x, y, width, height):
    """ Draw the drop-down menu for resolution selection. """
    global dropdown_open

    # Draw the drop-down button
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    screen.blit(selected_resolution_text, (x + 10, y + 5))

    if dropdown_open:
        # Draw the list of resolutions
        for i, res in enumerate(resolutions):
            pygame.draw.rect(screen, WHITE, (x, y + (i + 1) * height, width, height))
            res_text = font.render(f"{res[0]}x{res[1]}", True, BLACK)
            screen.blit(res_text, (x + 10, y + (i + 1) * height + 5))

def draw_checkbox(x, y, size, checked):
    """ Draws a checkbox at position (x, y) with the specified size and checked state. """
    pygame.draw.rect(screen, BLACK, (x, y, size, size), 2)  # Draw checkbox border
    if checked:
        pygame.draw.rect(screen, BLACK, (x + 5, y + 5, size - 10, size - 10))  # Check the box (fill it)

def draw_slider(x, y, width, height, knob_pos):
    """ Draws the volume slider. """
    pygame.draw.rect(screen, GRAY, (x, y, width, height))  # Draw slider track
    pygame.draw.circle(screen, HIGHLIGHT_COLOR, knob_pos, 10)  # Draw the knob

def handle_events():
    global dropdown_open, current_resolution, selected_resolution_text, screen, checkbox_checked, slider_knob_pos, slider_value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Handle click on drop-down button (toggle visibility of resolutions)
            if pygame.Rect(menu_x, menu_y, menu_width, menu_height).collidepoint(mouse_x, mouse_y):
                dropdown_open = not dropdown_open  # Toggle drop-down visibility

            # If the drop-down is open, check if a resolution is selected
            if dropdown_open:
                for i, res in enumerate(resolutions):
                    if pygame.Rect(menu_x, menu_y + (i + 1) * menu_height, menu_width, menu_height).collidepoint(mouse_x, mouse_y):
                        current_resolution = res
                        selected_resolution_text = font.render(f"Resolution: {current_resolution[0]}x{current_resolution[1]}", True, BLACK)
                        screen = pygame.display.set_mode(current_resolution)  # Update the screen size
                        dropdown_open = False  # Close the drop-down menu

            # Handle click on fullscreen checkbox
            if pygame.Rect(checkbox_x, checkbox_y, checkbox_size, checkbox_size).collidepoint(mouse_x, mouse_y):
                checkbox_checked = not checkbox_checked  # Toggle checkbox state
                if checkbox_checked:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Switch to fullscreen
                    selected_resolution_text = font.render(f"Resolution: {screen.get_size()[0]}x{screen.get_size()[1]}", True, BLACK)
                else:
                    screen = pygame.display.set_mode(current_resolution)  # Switch back to windowed mode
                    selected_resolution_text = font.render(f"Resolution: {screen.get_size()[0]}x{screen.get_size()[1]}", True, BLACK)

            # Handle click on the volume slider (if within the slider's area)
            if pygame.Rect(slider_x, slider_y, slider_width, slider_height).collidepoint(mouse_x, mouse_y):
                new_x = max(slider_x, min(mouse_x, slider_x + slider_width))
                slider_knob_pos[0] = new_x
                slider_value = (slider_knob_pos[0] - slider_x) / slider_width
                pygame.mixer.music.set_volume(slider_value)  # Update volume based on slider

        if event.type == pygame.MOUSEMOTION:
            # Handle dragging the volume slider knob
            if event.buttons[0]:  # Left mouse button is being held down
                if pygame.Rect(slider_x, slider_y, slider_width, slider_height).collidepoint(event.pos):
                    new_x = max(slider_x, min(event.pos[0], slider_x + slider_width))
                    slider_knob_pos[0] = new_x
                    slider_value = (slider_knob_pos[0] - slider_x) / slider_width
                    pygame.mixer.music.set_volume(slider_value)  # Update volume based on slider


def settings():

    # Main game loop
    running = True
    while running:
        screen.fill(WHITE)

        handle_events()  # Handle events such as clicks

        # Draw the volume slider
        draw_slider(slider_x, slider_y, slider_width, slider_height, slider_knob_pos)
        volume_text = font.render(f"Volume: {int(slider_value * 100)}%", True, BLACK)
        screen.blit(volume_text, (slider_x + slider_width + 10, slider_y))

        # Draw the resolution drop-down menu
        draw_dropdown(menu_x, menu_y, menu_width, menu_height)

        # Draw the fullscreen checkbox
        checkbox_text = font.render("Fullscreen", True, BLACK)
        screen.blit(checkbox_text, (checkbox_x + checkbox_size + 10, checkbox_y + 5))
        draw_checkbox(checkbox_x, checkbox_y, checkbox_size, checkbox_checked)

        pygame.display.flip()
