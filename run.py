import pygame
from pygame import *
from Classes.Snake import Snake
from Classes.Menu import Menu
from Classes.Button import Button
from Classes.Tile import Tile

FPS = 30
win_weight, win_height = 800, 600

pygame.init()  # инициализацияb
pygame.font.init()
snake = Snake(4, 4)
menu = Menu()

display = pygame.display.set_mode((win_weight, win_height))  # создание окна
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

done = False
while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.update()
    clock.tick(FPS)
    pygame.font.quit()
