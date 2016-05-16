import math
import os
import json
import pygame
from settings import *

DIR = ".."


location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)


def play_music(name):
    try:
        prepare_music(load_music(name))  # Проигрываем музыку.
    except KeyboardInterrupt:
        # Если пользователь прервёт проигрывание.
        # Завершаем проигрывание, как положено.
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit


def prepare_music(music_file):
    clock = pygame.time.Clock()  # Инициализируе часы.
    try:
        pygame.mixer.music.load(music_file)  # Загружае файл.
        print("Music file %s loaded!" % music_file)
    except pygame.error:  # Ловим ошибки загрузки
        print("File %s not found! (%s)" % (music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()  # Проигрываем
    while pygame.mixer.music.get_busy():  # Ожидаем завершение проигрывания
        clock.tick(30)  # Запускаем задержку - разгрузить процессор.


def load_music(name):
    music_file = os.path.join(MUSIC_DIR, name)  # Определяе какой файл проигрывать

    # Устанавливаем параметры Микшера.
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get right sound)
    # Инициализируем микшер.
    pygame.mixer.init(freq, bitsize, channels, buffer)

    pygame.mixer.music.set_volume(0.01)  # Устанавливаем грокость (максимум - 1).
    return music_file


def load_image(name, alpha_cannel):
    fullname = os.path.join(IMAGES_DIR, name)  # Указываем путь к папке с картинками

    try:
        image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    except pygame.error:  # Если картинки нет на месте
        print("Cannot load image:", name)
        return 0
    if alpha_cannel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


def max_top(top_l):
    lst = []
    for text in top_l:
        lst.append(text['score'])
    return max(lst)


def index(list, el):
    return print(list.index(el))


def save(data, file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()


def clear():
    """
    Очищает консоль
    Не работает в консоли PyCharm'a
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_full_name(people):
    return "%s %s %s" % (people["name"], people["middle_name"], people["surname"])


def search(peoples_list, **kwargs):
    """
    :param peoples_list: список людей, в котором производится поиск. format: [{}, {}, ...]
    :param kwargs: набор именованных параметров поиска
    :return: Возвращает список людей(словари) с заданными именованными параметрами
    """
    return [people for people in peoples_list
            if (people['name'] == kwargs['name'] if kwargs.get('name') else True)
            and (people['surname'] == kwargs['surname'] if kwargs.get('surname') else True)
            and (people['class'] == kwargs['class_room'] or kwargs['class_room'] in people['class']
                 if kwargs.get('class_room') else True)]


def print_table(data, num_columns=1, num_sep=10, sort=False, dir_output='line'):
    """
    Выводит на печать указанную псследовательность в несколько столбиков
    :param data: последовательность
    :param num_columns: ко-во столбиков
    :param num_sep: кол-во пробелов между столбиками
    :param dir_output: направление вывода. line - по строкам / column - по столбикам
    """
    if sort:
        pass  # TODO: дописать сортировку   # это не к нам

    n, line = 0, ""
    if dir_output == 'column':
        num_in_column = math.ceil(len(data)/num_columns)
        print(num_in_column)
        i = -1
        go = True
        try:
            while go:
                i += 1
                line = ''
                j = 0
                if i + 1 > num_in_column:
                    break
                while j < num_columns:
                    line += data[i + j * num_in_column] + " " * num_sep
                    j += 1

                print(line)
        except IndexError:
            if line:
                print(line)
    else:
        for el in data:
            n += 1
            if n <= num_columns:
                line += el + " " * num_sep
            else:
                print(line)
                n, line = 0, ""
        else:
            if line:
                print(line)


if __name__ == "__main__":
    print_table([
                    "5 А", "5 Б", "5 В", "5 Г",
                    "6 А", "6 Б", "6 В", "6 Г",
                    "7 А", "7 Б", "7 В", "7 Г",
                ], num_columns=3, dir_output='column')