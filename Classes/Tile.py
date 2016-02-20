import pygame
from pygame import *


class Tile:
    def __init__(self, pos, size):
        self.w = size[0]
        self.h = size[1]
        self.i = pos[0] * self.w   # индекс
        self.j = pos[1] * self.h   # высота в списке
        self.image = Surface(size)
        self.color = 0xFFEECCF0
        self.draw()

    def draw(self):
        pygame.draw.rect(self.image, self.color, ((0, 0), (self.w, self.h)))

    def render(self, screen):
        screen.blit(self.image, (0, 0 + self.h))