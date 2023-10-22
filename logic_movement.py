from constant import *


class Movement(object):
    ''' ЭТОТ КЛАСС НЕСЁТ В СЕБЕ ВСЕ ФУНКЦИИ СВЯЗАННЫЕЕ С ДВИЖЕНИЕМ ОБЪЕКТА В ЛОКАЛЬНЫХ КООРДИНАТАХ '''
    def __init__(self):
        pass

    def movement(self, position_local, speed_vector, rotate):  # метод в котором мы обрабатываем движение
        if rotate == 0:
            position_local = int(position_local[0]), int(position_local[1] + 2 * speed_vector)
        if rotate == 1:
            position_local = int(position_local[0] + speed_vector), int(position_local[1] + 2 * speed_vector)
        if rotate == 2:
            position_local = int(position_local[0] + 2 * speed_vector), int(position_local[1] + speed_vector)
        if rotate == 3:
            position_local = int(position_local[0] + 2 * speed_vector), int(position_local[1])
        if rotate == 4:
            position_local = int(position_local[0] + 2 * speed_vector), int(position_local[1] - speed_vector)
        if rotate == 5:
            position_local = int(position_local[0] + speed_vector), int(position_local[1] - 2 * speed_vector)
        if rotate == 6:
            position_local = int(position_local[0]), int(position_local[1] - 2 * speed_vector)
        if rotate == 7:
            position_local = int(position_local[0] - speed_vector), int(position_local[1] - 2 * speed_vector)
        if rotate == 8:
            position_local = int(position_local[0] - 2 * speed_vector), int(position_local[1] - speed_vector)
        if rotate == 9:
            position_local = int(position_local[0] - 2 * speed_vector), int(position_local[1])
        if rotate == 10:
            position_local = int(position_local[0] - 2 * speed_vector), int(position_local[1] + speed_vector)
        if rotate == 11:
            position_local = int(position_local[0] - speed_vector), int(position_local[1] + 2 * speed_vector)
        return position_local

    def fix(self, position_local, speed_vector):  # метод в котором мы проверяем потенциальную ошибку выхода за карту
        if position_local[0] < 0:
            position_local = 1, position_local[1]
            speed_vector = 00

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

    def collision_wall(self, position_local, speed_vector, grid, rotate):  # проверяем возможное столкновение со "стеной"
        if 2 <= position_local[0] <= 148 and 2 <= position_local[1] <= 148:
            possible_position = self.movement(position_local, speed_vector, rotate=rotate)
            if grid[(possible_position)][1] != 0:
                 speed_vector = 0
            return speed_vector
        else:
            return speed_vector