import pygame, os , sys

randomize = 0
(FPS, window_width, window_height) = (30, 400, 300)

pygame.init()  # инициализацияb
pygame.font.init()
display = pygame.display.set_mode((window_width, window_height))  # создание окна
screen = pygame.display.get_surface()
# tmp = screen.convert()
# caption = pygame.display.get_caption()
# flags = screen.get_flags()
# screen = pygame.display.set_mode((window_width, window_height), flags^FULLSCREEN)

done = False
clock = pygame.time.Clock()
while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обрабоccтка события "Закрытие окна"
            done = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
            if e.key == pygame.K_END:
                # run()
                pass
                # os.system('Snake.py')
    pygame.display.update()
    clock.tick(FPS)
    pygame.font.quit()
