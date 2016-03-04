import collections
# print(filter(lambda x: x > 0, [1, -2, 3]))     # сумма с отсортом отрицательных чисел


# def next(lst):               # Получает список клеток змейки и возвращает новую клетку хвоста
#     if lst[len(lst) - 1][0] == lst[len(lst) - 2][0]:
#         x = lst[len(lst) - 1][0]
#         if lst[len(lst) - 2][1] < lst[len(lst) - 1][1]:
#             y = lst[len(lst) - 1][1] + 1
#         else:
#             y = lst[len(lst) - 1][1] - 1
#     if lst[len(lst) - 1][1] == lst[len(lst) - 2][1]:
#         y = lst[len(lst) - 1][1]
#         if lst[len(lst) - 2][0] < lst[len(lst) - 1][0]:
#             x = lst[len(lst) - 1][0] + 1
#         else:
#             x = lst[len(lst) - 1][0] - 1
#     return x, y
#
# lst = [(1, 2), (2, 2), (2, 2), (3, 2)]
# print(next(lst))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


points_list = [Point(5, 2), Point(1, 2), Point(1, 2), Point(1, 3)]

if len([el for el in points_list if points_list.count(el) > 1]) > 1:
    print("True")
else:
    print("False")