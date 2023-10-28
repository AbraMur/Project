from numpy import floor
from perlin_noise import PerlinNoise
from constant import numbers_height_grid, numbers_width_grid
import random


def perlin_generate(seed):
    # генерация основного шума и параметризация
    noise = PerlinNoise(octaves=2, seed=seed)  # 4522
    elevation = 1  # высота
    chunk_size = 24  # размер чанка
    terrain_width = max(numbers_width_grid, numbers_height_grid) + 1  # размер карты

    # генерация матрицы для представления ландшафта
    landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]

    for position in range(terrain_width ** 2):
        # вычисление высоты y в координатах (x, z)
        x = floor(position / terrain_width)
        z = floor(position % terrain_width)
        y = floor(noise([x / chunk_size, z / chunk_size]) * elevation)
        landscale[int(x)][int(z)] = int(y)

    altitude_L = list(landscale)  # высота

    return altitude_L