import pygame
import sys
import os
import json

win_weigh = 1000
win_heigh = 700
DIR = '..'


def form(name, score):
    sym = 30 - len(name)
    return name, ' '*sym, score


class Top_records:
    def __init__(self):
        self.students_data = json.load(open(os.path.join(DIR, 'Top_Records.json'), 'r'))
        self.done = True
        self.lst = []

    def events(self, event):
        pass

    def render(self, screen):
        pass

    def read(self):
        top = json.load(open(os.path.join(DIR, 'Top_Records.json'), 'r'))

        for player in top:
            print('%s %s %s' % (form(player['name'], player['score'])))

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