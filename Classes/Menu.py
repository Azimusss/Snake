import pygame, sys, os
from pygame import *
from Classes.Button import Button
from Classes.Snake import Snake
FPS = 30
win_weight, win_height = 1000, 700
TILE_SIZE = 20
tile_wight = 40
tile_height = 30
field_width = tile_wight * TILE_SIZE
field_height = tile_height * TILE_SIZE


class Menu:
    def __init__(self):
        pygame.display.set_mode((win_weight, win_height))  # создание окна
        self.start_b = Button(('button_on.png', 'button_hover.png', 'button_click.png'),
                              path='../images/Buttons', pos=(410, 224), text='Start', function=self.start_game)
        self.top_b = Button(('button_on.png', 'button_hover.png', 'button_click.png'),
                              path='../images/Buttons', pos=(410, 287), text='Top Records', function=None)
        self.setting_b = Button(('button_on.png', 'button_hover.png', 'button_click.png'),
                              path='../images/Buttons', pos=(410, 350), text='Setting', function=None)
        self.exit_b = Button(('button_on.png', 'button_hover.png', 'button_click.png'),
                              path='../images/Buttons', pos=(410, 413), text='Exit', function=self.close)
        self.done = True

    def close(self):
        sys.exit()

    def update(self):
        pass

    def events(self, event):
        self.start_b.event(event)
        self.setting_b.event(event)
        self.top_b.event(event)
        self.exit_b.event(event)

    def render(self, screen):
        self.start_b.render(screen)
        self.setting_b.render(screen)
        self.top_b.render(screen)
        self.exit_b.render(screen)

    def start_game(self):
        pygame.font.init()
        snake = Snake((4, 4), (0, 0, 0), (255, 255, 255),
                  (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
                  4, 4, menu=None)
        snake.run_snake()

    def run(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Menu')
        game_screen = pygame.Surface((win_weight, win_height))
        screen = pygame.display.get_surface()
        clock = pygame.time.Clock()
        while self.done:  # главный цикл программы
            for event in pygame.event.get():  # цикл обработки очереди событий окна
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                self.events(event)
            pygame.display.update()
            clock.tick(FPS)
            screen.fill((10, 20, 30))
            game_screen.fill((10, 20, 30))
            self.render(screen)


menu = Menu()
menu.run()