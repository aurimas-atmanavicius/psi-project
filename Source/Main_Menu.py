import pygame

def resize_with_aspect_ratio(image, max_width, max_height):
    original_width, original_height = image.get_size()
    scale = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)
    return pygame.transform.scale(image, (new_width, new_height))

def main_menu(screen, width, height):
    # Load the smaller logo for the main menu
    logo = pygame.image.load("../Graphics/Logo_main_screen.png")
    logo = resize_with_aspect_ratio(logo, 400, 200)  # Adjusted size for better fit

    # Button dimensions and positions
    button_height = 60
    button_spacing = 20  # Space between buttons
    button_width = 300
    logo_margin = 50  # Space between logo and buttons
    button_start_y = 300  # Adjust this value to lower the buttons

    buttons = [
        ("New Game", button_start_y),
        ("Continue", button_start_y + (button_height + button_spacing) * 1),
        ("Settings", button_start_y + (button_height + button_spacing) * 2),
        ("Scoreboard", button_start_y + (button_height + button_spacing) * 3),
        ("Exit", button_start_y + (button_height + button_spacing) * 4),
    ]

    running = True
    while running:
        screen.fill((255, 255, 255))  # White background

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for text, y in buttons:
                    button_rect = pygame.Rect((width - button_width) // 2, y, button_width, button_height)
                    if button_rect.collidepoint(mouse_pos):
                        if text == "Exit":
                            running = False

        # Draw the logo
        screen.blit(logo, ((width - logo.get_width()) // 2, 50))  # Move the logo higher

        # Draw buttons
        for text, y in buttons:
            button_rect = pygame.Rect((width - button_width) // 2, y, button_width, button_height)
            color = (200, 200, 200) if button_rect.collidepoint(mouse_pos) else (150, 150, 150)
            pygame.draw.rect(screen, color, button_rect, border_radius=10)  # Rounded corners for better visuals
            font = pygame.font.Font(None, 40)  # Font size
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button_rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
