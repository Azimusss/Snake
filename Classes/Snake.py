import pygame, sys, random, json, os
from pygame import *
import settings
from Classes.Point import Point

NORMAL, LEFT, RIGHT, UP, DOWN, APPEND = 0, 1, 2, 3, 4, 5
FPS = 15
TILE_SIZE = 20
tile_wight = 50
tile_height = 35
field_width = tile_wight * TILE_SIZE
field_height = tile_height * TILE_SIZE


class Snake:
    def __init__(self, pos_text, color, color_rect, keys, start_x=0, start_y=0, menu=None):
        self.k_left = keys[0]
        self.k_right = keys[1]
        self.k_up = keys[2]
        self.k_down = keys[3]
        self.state = NORMAL
        self.color = color
        self.pos_text = pos_text
        self.color_rect = color_rect
        self.links = [Point(start_x, start_y), Point(start_x, start_y + 1),
                      Point(start_x, start_y + 2), Point(start_x, start_y + 3)]
        self.menu = menu
        self.food = Point(-1, -1)
        self.link_size = (TILE_SIZE, TILE_SIZE)
        self.link_img = pygame.Surface(self.link_size)
        self.i = 0
        self.field_size = Point(tile_wight, tile_height)
        with open(os.path.join(settings.DATA_DIR, 'Top_Records.json')) as f:
            self.top = json.load(f)
        self.done = False

        self.draw_link()
        self.create_food()
        self.counter_top()

    def draw_link(self):
        pygame.draw.rect(self.link_img, self.color, ((0, 0), self.link_size))
        pygame.draw.rect(self.link_img, self.color_rect, ((0, 0), self.link_size), 1)

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
            if event.key == self.k_left:
                if self.state != RIGHT:
                    self.state = LEFT
            if event.key == self.k_right:
                if self.state != LEFT:
                    self.state = RIGHT
            if event.key == self.k_up:
                if self.state != DOWN:
                    self.state = UP
            if event.key == self.k_down:
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
        screen.blit(text, self.pos_text)

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
            print("(", self.food, ")")
        else:
            self.create_food()

    def eat(self):
        if self.food == self.links[1]:
            self.create_food()
            self.longer()

    def game_over(self):
        from Classes.Menu import Menu
        self.done = True
        menu = Menu()
        menu.run()

    def counter_top(self):
        if len(self.top) > 9:
            rd_top = self.top[0:9]

    def run_snake(self):
        game_screen = pygame.Surface((field_width, field_height))
        display = pygame.display.set_mode((field_width, field_height))  # создание окна
        screen = pygame.display.get_surface()
        clock = pygame.time.Clock()
        while not self.done:  # главный цикл программы
            for e in pygame.event.get():  # цикл обработки очереди событий окна
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                self.events(e)

            pygame.display.update()
            clock.tick(FPS)
            screen.fill((10, 20, 30))
            game_screen.fill((10, 20, 30))
            try:
                self.update()
            except ValueError:
                print("You Lose")
                self.game_over()
                # sys.exit()
            self.render(game_screen)
            pygame.draw.line(game_screen, (0, 255, 0), (0, 0), (field_width, 0))
            display.blit(game_screen, (0, TILE_SIZE))
            pygame.display.flip()

if __name__ == "__main__":
    pygame.font.init()
    snake = Snake((4, 4), (0, 0, 0), (255, 255, 255),
                  (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
                  4, 4, menu=None)
    snake1 = Snake((983, 4), (255, 255, 255), (0, 0, 0),
                   (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN),
                   46, 4, menu=None)
    game_screen = pygame.Surface((field_width, field_height))
    display = pygame.display.set_mode((field_width, field_height))  # создание окна
    pygame.display.set_caption('Snake')
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    print(field_height / TILE_SIZE, field_width / TILE_SIZE)
    done = False
    while not done:  # главный цикл программы
        for e in pygame.event.get():  # цикл обработки очереди событий окна
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    sys.exit()
            snake.events(e)
            snake1.events(e)

        pygame.display.update()
        clock.tick(FPS)
        screen.fill((10, 20, 30))
        game_screen.fill((10, 20, 30))
        try:
            snake.update()
            snake1.update()
        except ValueError:
            print("You Lose")
            sys.exit()
        snake.render(game_screen)
        snake1.render(game_screen)
        pygame.draw.line(game_screen, (0, 255, 0), (0, 0), (field_width, 0))
        display.blit(game_screen, (0, TILE_SIZE))
        pygame.display.flip()
