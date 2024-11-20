import pygame
# import time

# pygame.init()
# screen_width = 1280
# screen_height = 720
# screen = pygame.display.set_mode((screen_width, screen_height))
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((255, 255, 255))
#     #screen.blit(image, ((screen_width - image.get_width()) // 2, (screen_height - image.get_height()) // 2))
#     pygame.display.flip()

# pygame.quit()


class OptionBox():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected = 0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))
            outer_rect = (self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1

# screen_width = 1280
# screen_height = 720
#screen = pygame.display.set_mode((screen_width, screen_height))

resolutions = [
    "1280x720",
    "1920x1080"
]

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((int(resolutions[0].split("x")[0]), int(resolutions[0].split("x")[1])))

list1 = OptionBox(
    40, 40, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
    resolutions)

run = True
while run:

    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        print(selected_option)
        window = pygame.display.set_mode((int(resolutions[selected_option].split("x")[0]), int(resolutions[selected_option].split("x")[1])))

    # print(window.get_height())
    window.fill((255, 255, 255))
    list1.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
