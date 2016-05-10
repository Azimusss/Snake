import pygame, sys, random
from Classes.Snake import Snake
from Classes.Menu import Menu
from Classes.Top_records import Top
FPS = 30
win_weight, win_height = 400, 500
TILE_SIZE = 20
tile_wight = 40
tile_height = 30
field_width = tile_wight * TILE_SIZE
field_height = tile_height * TILE_SIZE


class Run:
    def __init__(self):
        self.app_state = 'menu'

    def run_menu(self):
        self.app_state = 'menu'
        pygame.font.init()
        game_screen = pygame.Surface((win_weight, win_height))
        display = pygame.display.set_mode((win_weight, win_height))  # создание окна
        screen = pygame.display.get_surface()
        clock = pygame.time.Clock()
        mn = Menu()
        mn.run()

    def run_snake(self):
        self.app_state = 'snake'
        self.done = False
        game_screen = pygame.Surface((field_width, field_height))
        display = pygame.display.set_mode((field_width, field_height))  # создание окна
        screen = pygame.display.get_surface()
        clock = pygame.time.Clock()
        snake = Snake((4, 4), (0, 0, 0), (255, 255, 255),
                  (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
                  4, 4, menu=None)
        snake.run_snake()

    def run_record_table(self):
        self.app_state = 'top_records'
        rec = Top()
        rec.run()

    def update(self):
        if self.app_state == 'menu':
            self.menu.update()
        if self.app_state == 'snake':
            self.snake.update()
        if self.app_state == 'top_records':
            self.records.update()

    def events(self, event):
        if self.app_state == 'menu':
            self.menu.events(event)
        if self.app_state == 'snake':
            self.snake.events(event)
        if self.app_state == 'top_records':
            self.records.events(event)

    def render(self, screen):
        if self.app_state == 'menu':
            self.menu.render(screen)
        if self.app_state == 'snake':
            self.snake.render(screen)
        if self.app_state == 'top_records':
            self.records.render(screen)

    def run(self):
        game_screen = pygame.Surface((field_width, field_height))
        display = pygame.display.set_mode((field_width, field_height))  # создание окна
        screen = pygame.display.get_surface()
        clock = pygame.time.Clock()

run = Run()
run.run_menu()