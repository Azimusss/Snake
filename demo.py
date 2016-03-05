import pygame


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Field:
    def __init__(self):
        self.field = pygame.Surface(())


class Snake:
    def __init__(self, w, h):
        self.links = []
        self.link_size = pygame.Rect(0, 0, w, h)
        self.link_img = pygame.Surface(self.link_size)  # draw


class Food:
    def __init__(self, x, y):
        self.pos = Point(x, y)
        self.img = pygame.Surface(self.pos)  # draw


if __name__ == '__main__':
    pass