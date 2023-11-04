from constant import *
import math


class Movement(object):
    ''' ЭТОТ КЛАСС НЕСЁТ В СЕБЕ ВСЕ ФУНКЦИИ СВЯЗАННЫЕ С ДВИЖЕНИЕМ ОБЪЕКТА В ЛОКАЛЬНЫХ КООРДИНАТАХ '''

    def __init__(self):
        pass

    def movement(self, position_local, speed_vector, rotate):  # метод в котором мы обрабатываем движение
        pi = math.pi
        position_local = int(position_local[0] + round(math.sin(pi / 6 * rotate) * 2) * speed_vector), \
                           int(position_local[1] + round(math.cos(pi / 6 * rotate) * 2) * speed_vector)
        return position_local

    def fix(self, position_local, speed_vector):  # метод в котором мы проверяем потенциальную ошибку выхода за карту
        if position_local[0] < 0:
            position_local = 1, position_local[1]
            speed_vector = 0

        if position_local[0] > numbers_width_grid:
            position_local = numbers_width_grid - 1, position_local[1]
            speed_vector = 0

        if position_local[1] < 0:
            position_local = position_local[0], 1
            speed_vector = 0

        if position_local[1] > numbers_height_grid:
            position_local = position_local[0], numbers_height_grid - 1
            speed_vector = 0

        return position_local, speed_vector
