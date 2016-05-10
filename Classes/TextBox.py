# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


def get_key():
    """
    Получает нажатую клавишу
    """
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


def display_box(screen, message):
    """
    Принимает screen и приветственное сообшение(name)
    """
    """
    Возвращает картинку с текстом
    """
    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(screen, (0, 0, 0),  # <= цвет
                     ((screen.get_width() / 2) - 100,
                      (screen.get_height() / 2) - 10,
                      200, 20), 0)  # <= Прямоугольник ввода(внутренний)
    pygame.draw.rect(screen, (255, 255, 255),  # <= цвет
                     ((screen.get_width() / 2) - 102,
                      (screen.get_height() / 2) - 12,
                      204, 24), 1)  # <= Рамка прямоугольника ввода
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()


def ask(screen, question):
    """
    Args:
        screen: screen
        question: Вопрос
    Returns: Ответ
    """
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": ")
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + str.join("", current_string))
    return str.join("", current_string)


def main():
    screen = pygame.display.set_mode((1000, 700))
    return ask(screen, "Name")


if __name__ == '__main__':
    answer = main()
    print(answer)