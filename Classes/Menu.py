import pygame, sys, os
from pygame import *
from Classes.Button import Button
FPS = 30
win_weight, win_height = 800, 600


class Menu:
    def __init__(self):
        self.start = Button("start")
        self.start = Button("settings")
        self.start = Button("Exit")

    def update(self):
        pass

    def events(self, event):
        pass

    def render(self, screen):
        pass

pygame.font.init()
snake = Menu(4, 4)
game_screen = pygame.Surface((win_weight, win_height))
display = pygame.display.set_mode((win_weight, win_height))  # создание окна
screen = pygame.display.get_surface()
clock = pygame.time.Clock()