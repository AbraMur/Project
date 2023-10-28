import pygame
from constant import *
from grid import Grid
from logic_movement import Movement
from perlin_generate import *
from assets import *
from tank import Tank
from transform_perlin_noise import Grid_visual


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
        self.movement = Movement()  # переменная класса мовемент ( движение )
        self.motion = 0  # вектор "движения"
        seed = random.randint(1000, 3000)
        self.heights = perlin_generate(seed)

        self.heights_n = Grid_visual(position=(0, 0), heights=self.heights)
        heights = self.heights_n.transform((0, 0))

        self.grid.generate(heights)
        self.rotate = 0
        self.grid_dict = self.grid.get()  # мы получаем сетку

        self.position_local = x_start_local, y_start_local

        self.tank = Tank(screen=self.screen)

        self.tank_box = self.tank.tank_collision_pos(self.position_local, self.rotate)

    def setup(self):
        while self.grid_dict[self.position_local][1] != 0:
            heights = self.heights_n.transform((self.position_local[0] - x_start_local, self.position_local[1] - y_start_local))
            self.grid.generate(heights)
            self.position_local = random.randint(1, numbers_height_grid), random.randint(1, numbers_width_grid)


    def run(self):
        self.setup()
        while self.running:
            for event in pygame.event.get():
                self.event_handler(event)

            self.tank_box = self.tank.tank_collision_pos(self.position_local, self.rotate)
            for pos in self.tank_box:
                self.motion = self.movement.collision_wall(pos, self.motion, self.grid_dict, self.rotate)
            self.position_local = self.movement.movement(self.position_local, self.motion, self.rotate)

            heights = self.heights_n.transform((self.position_local[0] - x_start_local, self.position_local[1] - y_start_local))
            self.grid.generate(heights)

            self.position_local, self.motion = self.movement.fix(self.position_local, self.motion)
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop()
            if event.key == pygame.K_w:
                self.motion = (self.motion - acceleration)
            if event.key == pygame.K_a:
                self.rotate = (self.rotate + 1) % 12
            if event.key == pygame.K_d:
                self.rotate = (self.rotate - 1) % 12
            if event.key == pygame.K_s:
                self.motion = (self.motion + acceleration)
            if event.key == pygame.K_SPACE:
                self.motion = 0

    def draw(self):
        self.screen.fill(WHITE)

        if bool(abs(self.motion)):
            self.tank.tank_drive(center_tank=self.grid_dict[self.position_local][0], rotate=self.rotate, motion = self.motion)
        else:
            self.tank.tank_stand(center_tank=self.grid_dict[self.position_local][0], rotate=self.rotate)

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
