import pygame, sys
from pygame import *

FIELD_SIZE = 2, 10
FPS = 30
NORMAL, LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3, 4
TILE_SIZE = 20

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, start_x=0, start_y=0):
        self.state = NORMAL
        self.links = []
        self.links.append(Point(start_x, start_y))
        self.links.append(Point(2, 3))
        self.links.append(Point(2, 4))
        self.links.append(Point(2, 5))
        self.links.append(Point(2, 6))
        # self.links.append([2, 3])
        # self.links.append([2, 4])
        # self.links.append([2, 5])
        # self.links.append([2, 6])
        self.link_size = (TILE_SIZE, TILE_SIZE)
        self.link_img = pygame.Surface(self.link_size)
        self.draw_link()
        self.i = 0

    def draw_link(self):
        pygame.draw.rect(self.link_img, (0, 0, 200), ((0, 0), self.link_size))
        pygame.draw.rect(self.link_img, (255, 255, 255), ((0, 0), self.link_size), 1)

    def update(self, dt):
        self.i += 1
        if self.i == 2:
            self.move()
            self.i = 0
        # LEFT and RIGHT
        if self.links[0].x < 0:
            raise ValueError("Game Over")
        elif self.links[0].x * TILE_SIZE + TILE_SIZE > window_width:
            raise ValueError("Game Over")
        if self.links[0].y < 0:
            raise ValueError("Game Over")
        elif self.links[0].y * TILE_SIZE + (TILE_SIZE * 2) > window_height:
            raise ValueError("Game Over")

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            # if self.state == RIGHT:
                if event.key == pygame.K_LEFT:
                    self.state = LEFT
            # if self.state == LEFT:
                if event.key == pygame.K_RIGHT:
                    self.state = RIGHT
            # if self.state == DOWN:
                if event.key == pygame.K_UP:
                    self.state = UP
            # if self.state == UP:
                if event.key == pygame.K_DOWN:
                    self.state = DOWN

    def render(self, screen):
        for link in self.links:
            screen.blit(self.link_img, (link.x * self.link_size[0], link.y * self.link_size[1]))

    def move(self):
        if self.state == RIGHT:
            self.links.insert(0, Point(self.links[0].x + 1, self.links[0].y))
        if self.state == LEFT:
            self.links.insert(0, Point(self.links[0].x - 1, self.links[0].y))
        if self.state == UP:
            self.links.insert(0, Point(self.links[0].x, self.links[0].y - 1))
        if self.state == DOWN:
            self.links.insert(0, Point(self.links[0].x, self.links[0].y + 1))
        if not self.state == NORMAL:
            self.links.pop()

    def debug(self):
        print(self.links)
        print(self.links[0].x)
        print(self.links[0].y)

window_width = 800
window_height = 600

snake = Snake(2, 2)
game_screen = pygame.Surface((window_width, window_height - TILE_SIZE))
# pygame.draw.rect(game_screen, (0, 200, 0), game_screen.get_rect(), 2)       # рамка вокруг Surface'а
display = pygame.display.set_mode((window_width, window_height))  # создание окна
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
        snake.events(e)

    pygame.display.update()
    clock.tick(FPS)
    screen.fill((10, 20, 30))
    game_screen.fill((10, 20, 30))
    try:
        snake.update(0)
    except ValueError:
        print("You Lose")
        sys.exit()
    snake.render(game_screen)
    pygame.draw.line(game_screen, (0, 255, 0), (0, 0), (window_width, 0))
    display.blit(game_screen, (0, TILE_SIZE))
    pygame.display.flip()