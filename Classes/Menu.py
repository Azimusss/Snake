import pygame, sys, os
from pygame import *
from Classes.Button import Button
FPS = 30
win_weight, win_height = 800, 600


class Menu:
    def __init__(self):
        self.start_b = Button(("button_hover.png", "button_hover.png", "button_hover.png"),
                              path='../images/Buttons', pos=(40, 40), text='Start')
        # self.setting_b = Button("settings")
        # self.exit_b = Button("Exit")

    def update(self):
        pass

    def events(self, event):
        self.start_b.event(event)

    def render(self, screen):
        # print("render")
        self.start_b.render(screen)

pygame.font.init()
game_screen = pygame.Surface((win_weight, win_height))
display = pygame.display.set_mode((win_weight, win_height))  # создание окна
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

menu = Menu()

done = False
while not done:  # главный цикл программы
    for event in pygame.event.get():  # цикл обработки очереди событий окна
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.update()
    clock.tick(FPS)
    screen.fill((10, 20, 30))
    game_screen.fill((10, 20, 30))
    menu.render(screen)
    menu.events(event)