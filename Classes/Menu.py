import pygame, sys, os
from pygame import *
from Classes.Button import Button
from Classes.Game import Game
FPS = 30
win_weight, win_height = 400, 400


class Menu:
    def __init__(self):
        self.start_b = Button(('button_on.png', 'button_hover.png', 'button_click.png'),
                              path='../images/Buttons', pos=(107, 115), text='Start', function=self.start_game)
        self.setting_b = Button(('button_on.png', 'button_hover.png', 'button_click.png'),
                              path='../images/Buttons', pos=(107, 178), text='Setting', function=None)
        self.exit_b = Button(('button_on.png', 'button_hover.png', 'button_click.png'),
                              path='../images/Buttons', pos=(107, 241), text='Exit', function=self.close)
        self.done = True

    def close(self):
        self.done = False

    def update(self):
        pass

    def events(self, event):
        self.start_b.event(event)
        self.setting_b.event(event)
        self.exit_b.event(event)

    def render(self, screen):
        self.start_b.render(screen)
        self.setting_b.render(screen)
        self.exit_b.render(screen)

    def start_game(self):
        # pass
        self.done = False
        game = Game()
        game.run()

    def run(self):
        while self.done:  # главный цикл программы
            for event in pygame.event.get():  # цикл обработки очереди событий окна
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                menu.events(event)
            pygame.display.update()
            clock.tick(FPS)
            screen.fill((10, 20, 30))
            game_screen.fill((10, 20, 30))
            menu.render(screen)


pygame.font.init()
game_screen = pygame.Surface((win_weight, win_height))
display = pygame.display.set_mode((win_weight, win_height))  # создание окна
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

menu = Menu()
menu.run()