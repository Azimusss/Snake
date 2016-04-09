import pygame
from Classes.Snake import Snake
import sys


class Game:
    def __init__(self):
        # TODO: вынести в файл с настройками
        self.FPS = 30
        win_weight, win_height = 800, 600
        self.done = True

        pygame.init()  # инициализацияb
        pygame.font.init()
        self.snake = Snake(4, 4)
        # menu = Menu()

        pygame.display.set_mode((win_weight, win_height))  # создание окна
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self):
        while self.done:  # главный цикл программы
            for e in pygame.event.get():  # цикл обработки очереди событий окна
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
            pygame.display.update()
            self.clock.tick(self.FPS)
            pygame.font.quit()


# if __name__ == "__main__":
#     game = Game()
#     game.run()