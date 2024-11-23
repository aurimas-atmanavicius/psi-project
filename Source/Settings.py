import pygame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HIGHLIGHT_COLOR = (0, 255, 0)

def draw_dropdown(screen, width, height, dropdown_font, menu_x, menu_y, menu_width, menu_height, resolutions, dropdown_open):
    """ Draw the drop-down menu for resolution selection. """
    # Draw the drop-down button
    text_surface = dropdown_font.render(f"Resolution: {screen.get_size()[0]}x{screen.get_size()[1]}", True, BLACK)
    pygame.draw.rect(screen, (150, 150, 150), (menu_x, menu_y, menu_width, menu_height), border_radius=10)
    screen.blit(text_surface, (menu_x + 10, menu_y + 5))

    if dropdown_open:
        # Draw the list of resolutions
        for i, res in enumerate(resolutions):
            pygame.draw.rect(screen, (255, 255, 255), (menu_x, menu_y + (i + 1) * menu_height, menu_width, menu_height))
            res_text = dropdown_font.render(f"{res[0]}x{res[1]}", True, (0, 0, 0))
            screen.blit(res_text, (menu_x + 10, menu_y + (i + 1) * menu_height + 5))

def draw_checkbox(screen, width, height, checkbox_x, checkbox_y, checkbox_size, checkbox_checked):
    """ Draws a checkbox at position (x, y) with the specified size and checked state. """
    pygame.draw.rect(screen, (0, 0, 0), (checkbox_x, checkbox_y, checkbox_size, checkbox_size), 2)  # Draw checkbox border
    if checkbox_checked:
        pygame.draw.rect(screen, (0, 0, 0), (checkbox_x + 5, checkbox_y + 5, checkbox_size - 10, checkbox_size - 10))  # Check the box (fill it)

def draw_slider(screen, width, height, slider_x, slider_y, slider_width, slider_height, slider_knob_pos):
    """ Draws the volume slider. """
    pygame.draw.rect(screen, GRAY, (slider_x, slider_y, slider_width, slider_height))  # Draw slider track
    pygame.draw.circle(screen, HIGHLIGHT_COLOR, slider_knob_pos, 10)  # Draw the knob

def main(screen, width, height, MUSIC_VOLUME):
    """ Settings window """
    font = pygame.font.SysFont(None, 40)

    # Resolution Drop down list
    resolutions = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]

    # Drop-down menu
    dropdown_font = pygame.font.SysFont(None, 40)
    list_resolution_strings = []
    for res in resolutions:
        list_resolution_strings.append(f"Resolution: {res[0]}x{res[1]}")
    menu_longest_string = max(list_resolution_strings, key=len)
    #menu_text = f"Resolution: {current_resolution[0]}x{current_resolution[1]}"
    menu_x = 50
    menu_y = 250
    text_surface = dropdown_font.render(menu_longest_string, True, BLACK)
    menu_width, _ = text_surface.get_size()
    menu_width += 5
    menu_height = 30
    dropdown_open = False

    # Checkbox dimensions and initial state for fullscreen toggle
    checkbox_x, checkbox_y = 50, 120
    checkbox_size = 30
    checkbox_checked = False  # Initially unchecked

    # Volume slider dimensions
    slider_x, slider_y = 50, 200
    slider_width = 300
    slider_height = 10
    slider_knob_pos = [slider_x + int(slider_width * 0.5), slider_y + slider_height // 2]
    slider_value = MUSIC_VOLUME  # Initial volume (50%)

    # Back button
    back_button_height = 60
    back_button_width = 120
    back_button_start_y = 0
    back_button_start_x = 0
    back_button_text = ("Back")

    running = True
    while running:
        screen.fill(WHITE)
        #####################################################
        # EVENTS                                            #
        #####################################################
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle "Back" button click
                if event.button == 1:
                    back_button_rect = pygame.Rect(back_button_start_x, back_button_start_y, back_button_width, back_button_height)
                    if back_button_rect.collidepoint(mouse_pos):
                        running = False

                # Handle click on drop-down button (toggle visibility of resolutions)
                if pygame.Rect(menu_x, menu_y, menu_width, menu_height).collidepoint(mouse_pos):
                    dropdown_open = not dropdown_open  # Toggle drop-down visibility

                # If the drop-down is open, check if a resolution is selected
                if dropdown_open:
                    for i, res in enumerate(resolutions):
                        if pygame.Rect(menu_x, menu_y + (i + 1) * menu_height, menu_width, menu_height).collidepoint(mouse_pos[0], mouse_pos[1]):
                            current_resolution = res
                            selected_resolution_text = font.render(f"Resolution: {current_resolution[0]}x{current_resolution[1]}", True, BLACK)
                            screen = pygame.display.set_mode(current_resolution)  # Update the screen size
                            dropdown_open = False  # Close the drop-down menu

                # Handle click on fullscreen checkbox
                if pygame.Rect(checkbox_x, checkbox_y, checkbox_size, checkbox_size).collidepoint(mouse_pos[0], mouse_pos[1]):
                    checkbox_checked = not checkbox_checked  # Toggle checkbox state
                    if checkbox_checked:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Switch to fullscreen
                        selected_resolution_text = font.render(f"Resolution: {screen.get_size()[0]}x{screen.get_size()[1]}", True, BLACK)
                    else:
                        screen = pygame.display.set_mode(current_resolution)  # Switch back to windowed mode
                        selected_resolution_text = font.render(f"Resolution: {screen.get_size()[0]}x{screen.get_size()[1]}", True, BLACK)

                # Handle click on the volume slider (if within the slider's area)
                if pygame.Rect(slider_x, slider_y, slider_width, slider_height).collidepoint(mouse_pos):
                    new_x = max(slider_x, min(mouse_pos[0], slider_x + slider_width))
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

        #####################################################
        # DRAW                                              #
        #####################################################

        # Draw "Back" button
        back_button_rect = pygame.Rect(back_button_start_x, back_button_start_y, back_button_width, back_button_height)
        color = (200, 200, 200) if back_button_rect.collidepoint(mouse_pos) else (150, 150, 150)
        pygame.draw.rect(screen, color, back_button_rect, border_radius=10)  # Rounded corners for better visuals
        font = pygame.font.Font(None, 40)  # Font size
        text_surface = font.render(back_button_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=back_button_rect.center)
        screen.blit(text_surface, text_rect)

        # Draw the volume slider
        draw_slider(screen, width, height, slider_x, slider_y, slider_width, slider_height, slider_knob_pos)
        volume_text = font.render(f"Volume: {int(slider_value * 100)}%", True, (0, 0, 0))
        screen.blit(volume_text, (slider_x + slider_width + 10, slider_y))

        # Draw the resolution drop-down menu
        draw_dropdown(screen, width, height, dropdown_font, menu_x, menu_y, menu_width, menu_height, resolutions, dropdown_open)

        # Draw the fullscreen checkbox
        checkbox_text = font.render("Fullscreen", True, (0, 0, 0))
        screen.blit(checkbox_text, (checkbox_x + checkbox_size + 10, checkbox_y + 5))
        draw_checkbox(screen, width, height, checkbox_x, checkbox_y, checkbox_size, checkbox_checked)

        pygame.display.flip()

    return screen.get_size()[0], screen.get_size()[1], MUSIC_VOLUME
