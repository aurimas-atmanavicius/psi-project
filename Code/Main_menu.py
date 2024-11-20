print("Sveiki komanda!")

import pygame
pygame.init()


screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Sveiki komanda")
screen = pygame.display.set_mode((screen_width, screen_height))


image = pygame.image.load("../Graphics/Logo_main_screen.png")
image = pygame.transform.scale(image, (800, 800))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(image, ((screen_width - image.get_width()) // 2, (screen_height - image.get_height()) // 2))
    pygame.display.flip()

pygame.quit()
exit()
