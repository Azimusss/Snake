import pygame
import sys
import os
import json

win_weigh = 1000
win_heigh = 700
DIR = '..'


class Text:
    """
    :param text
    :param text image
    """
    def __init__(self, text, screen, pos, color=(0, 255, 0), font_size=12):
        self.font = pygame.font.SysFont("Courier New", 12)
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

class Top_records:
    """
    Занимается загрузкой файла и отображает загруженную информацию
    """
    def __init__(self):
        self.done = True
        self.top = json.load(open(os.path.join(DIR, 'Top_Records.json'), 'r'))

    def form(self, name, score):
        sym = 30 - len(name)
        return name, ' '*sym, score

    def events(self, event):
        pass

    def render(self, screen):
        l = 40
        for text in self.top:
            print(text)
            text = Text(text, screen, (400, l))
            text.render()
            l += 30

    def run(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_mode((win_weigh, win_heigh))  # создание окна
        pygame.display.set_caption('Top Records')
        screen = pygame.display.get_surface()

        while self.done:  # главный цикл программы
            for event in pygame.event.get():  # цикл обработки очереди событий окна
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                self.events(event)
            pygame.display.update()
            screen.fill((10, 20, 30))
            self.render(screen)
            pygame.display.flip()

rec = Top_records()
rec.run()
rec.render()