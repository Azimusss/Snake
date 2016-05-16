import pygame
import sys
import os
import json
import settings
from utilities import *

FPS = 30
TILE_SIZE = 20
tile_wight = 40
tile_height = 30
field_width = tile_wight * TILE_SIZE
field_height = tile_height * TILE_SIZE


class Text:
    """
    :param text
    :param text image
    """
    def __init__(self, text, screen, pos, color=(0, 255, 0), font_size=20):
        self.font = pygame.font.SysFont("Courier New", font_size)
        self.text = self.font.render(str(text), 2, (0, 250, 0))
        self.screen = screen
        self.pos = pos
        self.color = color
        self.font_size = font_size

    def render(self):
        """
        Возвращает картинку с текстом
        """
        self.font.render(str(self.text), True, self.color)
        self.screen.blit(self.text, self.pos)


class Top:
    """
    Занимается загрузкой файла и отображает загруженную информацию
    """
    def __init__(self):
        self.done = True
        with open(os.path.join(settings.DATA_DIR, 'Top_Records.json')) as f:
            self.top = json.load(f)

    def events(self, event):
        pass

    def render(self, screen):
        l = 160
        for text in self.top:
            text = Text(text['name'], screen, (360, l), font_size=16)
            text.render()
            l += 30
        h = 160
        for text in self.top:
            text = Text(text['score'], screen, (590, h), font_size=16)
            text.render()
            h += 30

    def start_menu(self):
        from Classes.Menu import Menu
        pygame.font.init()
        game_screen = pygame.Surface((WIN_WIDHT, WIN_HEIGH))
        display = pygame.display.set_mode((WIN_WIDHT, WIN_HEIGH))  # создание окна
        screen = pygame.display.get_surface()
        clock = pygame.time.Clock()
        mn = Menu()
        mn.run()


    def run(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_mode((WIN_WIDHT, WIN_HEIGH))  # создание окна
        pygame.display.set_caption('Top Records')
        screen = pygame.display.get_surface()

        while self.done:  # главный цикл программы
            for event in pygame.event.get():  # цикл обработки очереди событий окна
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.start_menu()
                self.events(event)
            pygame.display.update()
            screen.fill((10, 20, 30))
            self.render(screen)
            pygame.display.flip()


if __name__ == '__main__':
    rec = Top()
    rec.run()