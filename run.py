import pygame, sys
from util import *

FPS = 40
RESX, RESX = 800, 600
NORMAL = 0
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
TILE_W, TILE_H = 40, 40
FPS = 30

class Snake:
    def __init__(self, pos, field, size):
        self.w = size[0]
        self.h = size[1]
        self.y = pos[0] * self.w   # индекс
        self.x = pos[1] * self.h   # высота в списке
        self.field = field
        self.image = pygame.Surface((20, 20))
        self.state = NORMAL
        self.field[pos[0] - 1][pos[1] - 1] = 's'
        self.image = pygame.Surface(size)
        self.color = 0xFFEECCF0
        self.score = 0
        self.update()
        self.draw()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.state = LEFT
            if event.key == pygame.K_RIGHT:
                self.state = RIGHT
            if event.key == pygame.K_UP:
                self.state = UP
            if event.key == pygame.K_DOWN:
                self.state = DOWN
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    def draw(self):
        pygame.draw.rect(self.image, self.color, ((0, 0), (self.w, self.h)))
        print(self.y, self.x)

    def render(self, screen):
        screen.blit(self.image, (self.x - self.h, self.y + self.h - self.w))

    def update(self):
        if self.state == LEFT:
            self.x - 1
        if self.state == RIGHT:
            self.x + 1
        if self.state == UP:
            self.y + 1
        if self.state == DOWN:
            self.y - 1

Field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

window_width = len(Field[0]) * TILE_W
window_height = len(Field) * TILE_H + TILE_H
display = pygame.display.set_mode((window_width, window_height))  # создание окна
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

Snake = Snake((2, 4), Field, (TILE_W, TILE_H))

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
    Snake.update()
    Snake.draw()
    pygame.font.quit()
    screen.fill((10, 20, 30))
    Snake.render(screen)
    pygame.display.flip()
    pygame.draw.line(screen, (0, 255, 0), (0, 40), (window_width, 40))