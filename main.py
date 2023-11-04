import pygame
from constant import *
from grid import Grid
from logic_movement import Movement
from perlin_generate import *
from tank import Tank
from transform_perlin_noise import Grid_visual
import math


class Game(object):
    '''
    ЭТО ОСНОВНОЙ КЛАСС В КОТОРОМ ПРОИСХОДЯТ ВСЕ СОБЫТИЯ, метод setup отвечает за начальные настройки,
    метод run отвечает за "бесконечный" цикл программы, метод event_handler отвечает за обработку событий игры,
    метод draw за отрисовку, ну а stop за остановку
    '''

    def __init__(self):
        self.clock = pygame.time.Clock()  # что бы плавно работало
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # что бы окошечко было
        self.running = True  # переменная что бы работал главный цикл
        self.grid = Grid()  # переменная класса сетки ( создаем сетку, получаем и тп )
        self.objects = []

        self.movement = Movement()  # переменная класса мовемент ( движение )  убрать класс мотион создать набор функций движения

        seed = random.randint(1000, 3000)  # это всё с сеткой связанно
        self.heights = perlin_generate(seed)  # это всё с сеткой связанно

        self.heights_n = Grid_visual(position=(0, 0), heights=self.heights) # это всё с сеткой связанно
        heights = self.heights_n.transform((0, 0)) # это всё с сеткой связанно

        self.grid.generate(heights)  # это всё с сеткой связанно

        self.grid_dict = self.grid.get()  # мы получаем сетку

        self.tank = Tank(game=self)  # ТАНК
        self.tank_box = self.tank.tank_collision_pos(self.tank.position)  # ТАНК

        self.objects.append(self.tank)
    def setup(self):
        while self.grid_dict[self.tank.position][1] != 0:
            self.tank.position = random.randint(1, numbers_height_grid), random.randint(1, numbers_width_grid)
            heights = self.heights_n.transform((self.tank.position[0] - x_start_local, self.tank.position[1] - y_start_local))
            self.grid.generate(heights)


    def run(self):
        self.setup()
        while self.running:
            for event in pygame.event.get():
                self.event_handler(event)

            self.update()

            self.tank_box = self.tank.tank_collision_pos(self.tank.position)


            if self.tank.can_drive():
                self.tank.position = self.movement.movement(self.tank.position, self.tank.speed, self.tank.rotate)

            heights = self.heights_n.transform((self.tank.position[0] - x_start_local, self.tank.position[1] - y_start_local))
            self.grid.generate(heights)

            self.tank.position, self.tank.speed = self.movement.fix(self.tank.position, self.tank.speed)

            for pos in self.tank_box:
                self.tank.speed = self.collision_wall(pos, self.tank.speed, self.grid_dict, self.tank.rotate)

            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

    def update(self):
        for obj in self.objects:
            obj.update()

    def movement_1(self, position_local, speed_vector, rotate):  # метод в котором мы обрабатываем движение
        pi = math.pi
        position_local = int(position_local[0] + round(math.sin(pi / 6 * rotate) * 2) * speed_vector), \
                           int(position_local[1] + round(math.cos(pi / 6 * rotate) * 2) * speed_vector)
        return position_local

    def collision_wall(self, position_local, speed_vector, grid, rotate):  # проверяем возможное столкновение со "стеной"
        if 2 <= position_local[0] <= 148 and 2 <= position_local[1] <= 148:
            possible_position = self.movement_1(position_local, speed_vector, rotate=rotate)
            if grid[(possible_position)][1] != 0:
                speed_vector = 0
            return speed_vector
        else:
            return speed_vector

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop()
        for obj in self.objects:
            obj.event_handler(event)

    def draw(self):
        self.screen.fill(WHITE)

        for obj in self.objects:
            obj.draw(self.screen)

        for i in range(numbers_width_grid + 1):
            for j in range(numbers_height_grid + 1):
                inf = self.grid_dict[(i, j)]
                color = (abs(inf[1] * 100), abs(inf[1] * 100), abs(inf[1] * 100))
                if inf[1]:
                    pygame.draw.circle(self.screen, color, inf[0], 3)
        
        for j in self.tank_box:
            pygame.draw.circle(self.screen, ORANGE, self.grid_dict[j][0], 3)

        # for i in range(numbers_height_grid + 1):
        #     pygame.draw.line(self.screen, ORANGE,[x0, y0+h*i/wl],[x0+width, y0+h*i/wl])
        #     pygame.draw.line(self.screen, ORANGE, [x0+h*i/hl, y0], [x0 + h * i / hl, y0 + width])

    def stop(self):
        self.running = False


if __name__ == '__main__':
    game = Game()
    game.run()
