import pygame, sys, random
from pygame import *
from Classes.Point import Point

NORMAL, LEFT, RIGHT, UP, DOWN, APPEND = 0, 1, 2, 3, 4, 5
FPS = 15
TILE_SIZE = 20
tile_wight = 40
tile_height = 30
field_width = tile_wight * TILE_SIZE
field_height = tile_height * TILE_SIZE


class Snake:
    def __init__(self, start_x=0, start_y=0, color=(100, 150, 200)):
        self.state = NORMAL
        self.color = color
        self.links = [Point(start_x, start_y), Point(start_x, start_y + 1),
                      Point(start_x, start_y + 2), Point(start_x, start_y + 3)]
        self.food = Point(-1, -1)
        self.link_size = (TILE_SIZE, TILE_SIZE)
        self.link_img = pygame.Surface(self.link_size)
        self.i = 0
        self.field_size = Point(tile_wight, tile_height)

        self.draw_link()

    def draw_link(self):
        pygame.draw.rect(self.link_img, self.color, ((0, 0), self.link_size))
        pygame.draw.rect(self.link_img, (255, 255, 255), ((0, 0), self.link_size), 1)

    def update(self):
        self.i += 1
        if self.i == 1:
            self.move()
            self.i = 0
        # LEFT and RIGHT
        if self.links[0].x < 0:
            raise ValueError("Game Over")
        elif self.links[0].x * TILE_SIZE + TILE_SIZE > field_width:
            raise ValueError("Game Over")
        # UP and DOWN
        if self.links[0].y < 0:
            raise ValueError("Game Over")
        elif self.links[0].y * TILE_SIZE + (TILE_SIZE * 2) > field_height:
            raise ValueError("Game Over")
        # COLLIDE SELF
        if len([el for el in self.links if self.links.count(el) > 1]) > 1:
            print([el for el in self.links if self.links.count(el) > 1])
            raise ValueError("Game Over")
        self.eat()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.state != RIGHT:
                    self.state = LEFT
            if event.key == pygame.K_RIGHT:
                if self.state != LEFT:
                    self.state = RIGHT
            if event.key == pygame.K_UP:
                if self.state != DOWN:
                    self.state = UP
            if event.key == pygame.K_DOWN:
                if self.state != UP:
                    self.state = DOWN
            if event.key == pygame.K_END:
                self.links.append(Point(*self.longer()))  # Добавление клетки
            if event.key == pygame.K_HOME:
                self.create_food()
            if event.key == pygame.K_DELETE:
                time.wait(1000)
            if event.key == pygame.K_INSERT:
                print(snake.links)

    def render(self, screen):
        for link in self.links:  # Отрисовка змея горыныча
            screen.blit(self.link_img, (link.x * self.link_size[0], link.y * self.link_size[1]))
            screen.blit(self.link_img, (self.food.x * self.link_size[0], self.food.y * self.link_size[1]))
        font = pygame.font.SysFont("Courier New", 12)
        text = font.render(str(len(self.links)), 2, (0, 250, 0))
        # pygame.draw.rect(screen, (0, 0, 255), ((0, 1), (field_width, field_height)), 1)
        # pygame.draw.rect(game_screen, (255, 0, 0), game_screen.get_rect(), 2)       # рамка вокруг Surface'а
        screen.blit(text, (5, 5))

    def move(self):
        if self.state == RIGHT:
            self.links.insert(0, Point(self.links[0].x + 1, self.links[0].y))
            self.links.pop()
        if self.state == LEFT:
            self.links.insert(0, Point(self.links[0].x - 1, self.links[0].y))
            self.links.pop()
        if self.state == UP:
            self.links.insert(0, Point(self.links[0].x, self.links[0].y - 1))
            self.links.pop()
        if self.state == DOWN:
            self.links.insert(0, Point(self.links[0].x, self.links[0].y + 1))
            self.links.pop()

    def longer(self):
        if self.links[len(self.links) - 1].x == self.links[len(self.links) - 2].x:
            x = self.links[len(self.links) - 1].x
            if self.links[len(self.links) - 2].y < self.links[len(self.links) - 1].y:
                y = self.links[len(self.links) - 1].y + 1
            else:
                y = self.links[len(self.links) - 1].y - 1
        if self.links[len(self.links) - 1].y == self.links[len(self.links) - 2].y:
            y = self.links[len(self.links) - 1].y
            if self.links[len(self.links) - 2].x < self.links[len(self.links) - 1].x:
                x = self.links[len(self.links) - 1].x + 1
            else:
                x = self.links[len(self.links) - 1].x - 1
        self.links.append(Point(x, y))
        return x, y

    def create_food(self):
        a = random.randint(0, tile_wight - 1)
        b = random.randint(0, tile_height - 2)
        point = Point(a, b)
        if point not in self.links:
            self.food = point
        else:
            self.create_food()

    def eat(self):
        if self.food == self.links[1]:
            self.create_food()
            self.longer()

    def run(self):
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
                snake.update()
            except ValueError:
                print("You Lose")
                print("You Highscore :", len(snake.links))
                sys.exit()
            snake.render(game_screen)
            pygame.draw.line(game_screen, (0, 255, 0), (0, 0), (field_width, 0))
            display.blit(game_screen, (0, TILE_SIZE))
            pygame.display.flip()

pygame.font.init()
snake = Snake(4, 4)
game_screen = pygame.Surface((field_width, field_height))
display = pygame.display.set_mode((field_width, field_height))  # создание окна
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

