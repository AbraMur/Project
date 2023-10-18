from constant import *


class Movement(object):
    ''' ЭТОТ КЛАСС НЕСЁТ В СЕБЕ ВСЕ ФУНКЦИИ СВЯЗАННЫЕЕ С ДВИЖЕНИЕМ ОБЪЕКТА В ЛОКАЛЬНЫХ КООРДИНАТАХ '''
    def __init__(self):
        pass

    def movement(self, position_local, speed_vector): # метод в котором мы обрабатываем движение
        position_local = int(position_local[0] + speed_vector[0]), int(position_local[1] + speed_vector[1])
        return position_local

    def fix(self, position_local, speed_vector): # метод в котором мы проверяем потенциальную ошибку выхода за карту
        if position_local[0] < 0:
            position_local = 1, position_local[1]
            speed_vector = 0, 0

        if position_local[0] > numbers_width_grid:
            position_local = numbers_width_grid - 1, position_local[1]
            speed_vector = 0, 0

        if position_local[1] < 0:
            position_local = position_local[0], 1
            speed_vector = 0, 0

        if position_local[1] > numbers_height_grid:
            position_local = position_local[0], numbers_height_grid - 1
            speed_vector = 0, 0

        return position_local, speed_vector

    def collision_wall(self, position_local, speed_vector, grid): # проверяем возможное столкновение со "стеной"
        if 1 <= position_local[0] <= 149 and 1 <= position_local[1] <= 149:
            possible_position = int(position_local[0] + speed_vector[0]), int(position_local[1] + speed_vector[1])
            if grid[(possible_position)][1] != 0:
                 speed_vector = 0,0
            return speed_vector
        else:
            return speed_vector