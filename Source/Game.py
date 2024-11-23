""" Main logic for the game """
import json
import random

import pygame

JSON_QUESTION_FILE = "../Levels/Test_level.json"

def read_json_questions_file(filename = "Test_level.json"):
    """
    Reads: default 'Test_level.json' or provided json file
    Returns its data
    """
    with open(filename, "r", encoding="utf8") as file:
        return json.load(file)

def play_10_random_questions(screen, width, height):
    """ Starts 10 questions Quiz game"""
    # Button dimensions and positions
    button_height = 60
    button_spacing = 20  # Space between buttons
    button_width = 300

    button_start_y = 300
    score = 0

    #####################################################
    data = read_json_questions_file(JSON_QUESTION_FILE)
    list_questions_index = []
    answer_buttons = []

    for _ in range(10):
        random_number = random.randrange(len(data))
        list_questions_index.append(random_number)

    for answer_index, answer in enumerate(data[list_questions_index[0]]["answers"]):
        answer_buttons.append((answer, button_start_y + (button_height + button_spacing) * answer_index))
    #####################################################

    #####################################################
    index = 0
    running = True
    while running:
        screen.fill((255, 255, 255))  # White background

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for text, y in answer_buttons.copy():
                    button_rect = pygame.Rect((width - button_width) // 2, y, button_width, button_height)
                    if button_rect.collidepoint(mouse_pos):
                        if text == data[list_questions_index[index]]["answers"][data[list_questions_index[index]]["correct_answer"]]:
                            index += 1
                            score += 1
                            answer_buttons = []
                            for answer_index, answer in enumerate(data[list_questions_index[index]]["answers"]):
                                answer_buttons.append((answer, button_start_y + (button_height + button_spacing) * answer_index))
                        else:
                            index += 1
                            answer_buttons = []
                            for answer_index, answer in enumerate(data[list_questions_index[index]]["answers"]):
                                answer_buttons.append((answer, button_start_y + (button_height + button_spacing) * answer_index))
                        if index == 9:
                            running = False

        # Draw Score
        font = pygame.font.Font(None, 40)  # Font size
        text_surface = font.render(f"Score: {score}", True, (0, 0, 0))
        text_width, _ = text_surface.get_size()
        screen.blit(text_surface, (0,0))

        # Draw Question
        font = pygame.font.Font(None, 50)  # Font size
        text_surface = font.render(data[list_questions_index[index]]["question"], True, (0, 0, 0))
        text_width, _ = text_surface.get_size()
        screen.blit(text_surface, ((width - text_width) // 2,150))

        # Draw buttons
        for text, y in answer_buttons:
            button_rect = pygame.Rect((width - button_width) // 2, y, button_width, button_height)
            color = (35, 150, 35) if button_rect.collidepoint(mouse_pos) else (150, 150, 150)
            pygame.draw.rect(screen, color, button_rect, border_radius=10)  # Rounded corners for better visuals
            font = pygame.font.Font(None, 40)  # Font size
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button_rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
    #####################################################
