import pygame
from pygame import *
from Classes.Snake import Snake


class Game:
    def __init__(self):
        self.snake = Snake(4, 4)

    def update(self):
        self.snake.update()

    def events(self, event):
        self.snake.events(event)

    def render(self, screen):
        self.snake.render(screen)