import pygame, os , random, sys


randomize = 0
(FPS, window_width, window_height) = (30, 1280, 720)
bg = pygame.image.load(os.path.join('images', 'Backgrounds', 'Background1.jpg'))
bg_rect = pygame.image.load(os.path.join('images', 'Backgrounds', 'Background_rected.jpg'))

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
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            screen.blit(bg_rect, (0, 0))
            print("Key Down")
        if e.type == pygame.KEYUP:  # Событие "Клавиша отжата"
            screen.blit(bg, (0, 0))
            print("Key Down")
        if e.type == pygame.MOUSEBUTTONDOWN:  # Событие "Клавиша мыши нажата"
            randomize = random.randint(1, 12)
            print("Randomed")
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
            if e.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.update()
    clock.tick(FPS)
    pygame.font.quit()
