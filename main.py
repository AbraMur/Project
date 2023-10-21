import pygame
from constant import *
from grid import Grid
from logic_movement import Movement
from perlin_generate import *
from assets import *
from tank import Tank



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
        self.motion_vector = 0, 0  # вектор "движения"
        seed = random.randint(1000, 3000)
        heights = perlin_generate(seed)
        self.grid.generate(heights)
        self.grid_dict = self.grid.get()  # мы получаем сетку
        self.position_local = random.randint(1, numbers_height_grid), random.randint(1, numbers_width_grid)

        self.tank = Tank(screen=self.screen)


    def setup(self):
        while self.grid_dict[self.position_local][1] != 0:
            self.position_local = random.randint(1, numbers_height_grid), random.randint(1, numbers_width_grid)

    def run(self):
        self.setup()
        while self.running:
            for event in pygame.event.get():
                self.event_handler(event)

            self.motion_vector = self.movement.collision_wall(self.position_local, self.motion_vector, self.grid_dict)
            self.position_local = self.movement.movement(self.position_local, self.motion_vector)
            self.position_local, self.motion_vector = self.movement.fix(self.position_local, self.motion_vector)
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
                self.motion_vector = self.motion_vector[0], self.motion_vector[1] - acceleration
            if event.key == pygame.K_a:
                self.motion_vector = self.motion_vector[0] - acceleration, self.motion_vector[1]
            if event.key == pygame.K_d:
                self.motion_vector = self.motion_vector[0] + acceleration, self.motion_vector[1]
            if event.key == pygame.K_s:
                self.motion_vector = self.motion_vector[0], self.motion_vector[1] + acceleration
            if event.key == pygame.K_SPACE:
                self.motion_vector = 0, 0

    def draw(self):
        self.screen.fill(WHITE)
        #  pygame.draw.circle(self.screen, BLACK, self.grid_dict[self.position_local][0], test_radius_object)
        if bool(abs(self.motion_vector[0])+abs(self.motion_vector[1])):
            self.tank.tank_drive(center_tank=self.grid_dict[self.position_local][0])
        else:
            self.tank.tank_stand(center_tank=self.grid_dict[self.position_local][0])

        # self.tank_rect = self.tank_sprite.get_rect(center=self.grid_dict[self.position_local][0])
        # self.screen.blit(self.tank_sprite, self.tank_rect)

        for i in range(numbers_width_grid + 1):
            for j in range(numbers_height_grid + 1):
                inf = self.grid_dict[(i, j)]
                color = (abs(inf[1] * 100), abs(inf[1] * 100), abs(inf[1] * 100))
                if inf[1]:
                    pygame.draw.circle(self.screen, color, inf[0], 3)

    def stop(self):
        self.running = False


if __name__ == '__main__':
    game = Game()
    game.run()
