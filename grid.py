from constant import *
from perlin_generate import *


# класс сетки
class Grid(object):
    '''  ВАЖНО ПОНИМАТЬ, ЧТО СЕТКА ИМЕЕТ ВИД dict[(local_x, local_y)] = ((global_x, global_y), heights)
    key = (local_x, local_y) values = ((global_x, global_y), heights)'''
    def __init__(self):  # создаем переменную "сетки", указываем её тип (словарь)
        self.grid = dict()

    def generate(self, heights_list):  # генерируем сетку, где ключ у нас локальные координаты, а значения это глобальные координаты и высота
        for i in range(numbers_width_grid + 1):
            for j in range(numbers_height_grid + 1):
                self.grid[(i, j)] = (x_global_coord_grid + width * i / numbers_width_grid - width / (numbers_width_grid * 2),
                                     y_global_coord_grid + height * j / numbers_height_grid - height / (numbers_height_grid * 2)), \
                                    heights_list[i][j]

    def get(self):  # получаем сетку по запросу
        return self.grid