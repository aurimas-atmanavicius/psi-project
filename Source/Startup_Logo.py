import pygame

def resize_with_aspect_ratio(image, max_width, max_height):
    original_width, original_height = image.get_size()
    scale = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)
    return pygame.transform.scale(image, (new_width, new_height))

def startup_screen(screen, width, height):
    # Load the logo
    logo = pygame.image.load("../Graphics/Logo_main_screen.png")
    logo = resize_with_aspect_ratio(logo, 600, 400)

    clock = pygame.time.Clock()

    # Fade-in effect
    for alpha in range(0, 256, 5):
        screen.fill((255, 255, 255))
        logo.set_alpha(alpha)
        screen.blit(logo, ((width - logo.get_width()) // 2, (height - logo.get_height()) // 2))
        pygame.display.flip()
        clock.tick(60)

    # Display the logo for 2 seconds
    pygame.time.delay(2000)
