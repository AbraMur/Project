import pygame
from constant import *


# класс, отвечающий за все, что связано с танком (анимации, движение, коллизия и т.п.)
class Tank(object):
    def __init__(self, game):
        self.speed = 0
        self.rotate = 0
        self.bullet_speed = 0
        self.position = x_start_local, y_start_local

        self.game = game
        self.tank_time = 0  # за анимацию отвечает
        self.speed_1 = 8  # максимальная скорость
        self.speed_tick = 0  # скорость

        self.tank_sprite_straight = [pygame.image.load('assets/tank/Straight/Sprite-0001.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0002.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0003.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0005.png')]  # модель танка при движении вперёд/назад

        self.tank_sprite_right = [pygame.image.load('assets/tank/Straight/Sprite-0001.png'),
                            pygame.image.load('assets/tank/Turn right/Sprite-0006.png'),
                            pygame.image.load('assets/tank/Turn right/Sprite-0007.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Turn right/Sprite-0008.png'),
                            pygame.image.load('assets/tank/Turn right/Sprite-0009.png')]  # модель танка при повороте направо

        self.tank_sprite_left = [pygame.image.load('assets/tank/Straight/Sprite-0001.png'),
                            pygame.image.load('assets/tank/Turn left/Sprite-0010.png'),
                            pygame.image.load('assets/tank/Turn left/Sprite-0011.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Turn left/Sprite-0012.png'),
                            pygame.image.load('assets/tank/Turn left/Sprite-0013.png')]  # модель танка при повороте налево

    def update(self, speed=0):
        # self.speed += speed
        self.speed_tick += 1
        if self.speed_tick == self.speed_1:
            self.speed_tick = 0

    def draw(self, screen):
        if bool(abs(self.speed)):
            self.tank_drive(center_tank=self.game.grid_dict[self.position][0], motion=self.speed)
        else:
            self.tank_stand(center_tank=self.game.grid_dict[self.position][0])

    def tank_front(self):  # движение танка назад
        self.speed += acceleration

    def tank_back(self):  # движение танка вперед
        self.speed -= acceleration

    def tank_rotate_right(self):  # поворот танка вправо
        self.rotate = (self.rotate + 1) % 12

    def tank_rotate_left(self):  # поворот танка влево
        self.rotate = (self.rotate - 1) % 12

    def event_handler(self, event):  # обработчик событий (отслеживает нажатие клавиш)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.tank_back()
            if event.key == pygame.K_a:
                self.tank_rotate_right()
            if event.key == pygame.K_d:
                self.tank_rotate_left()
            if event.key == pygame.K_s:
                self.tank_front()
            if event.key == pygame.K_SPACE:
                self.speed = 0

    def can_drive(self):
        return self.speed_tick == 0

    def tank_stand(self, center_tank):  # анимация танка, когда тот стоит
        rotate = self.rotate * delta

        tank_sprite = pygame.transform.rotate(self.tank_sprite_straight[self.tank_time], rotate)
        self.tank_rect = tank_sprite.get_rect(center=center_tank)
        self.game.screen.blit(tank_sprite, self.tank_rect)

    def tank_drive(self, center_tank, motion):  # анимация танка при движении
        rotate = self.rotate * delta
        sign = (motion > 0) - (motion < 0)

        self.tank_time = (self.tank_time + sign * 1) % 5
        tank_sprite = pygame.transform.rotate(self.tank_sprite_straight[self.tank_time], rotate)
        self.tank_rect = tank_sprite.get_rect(center=center_tank)
        self.game.screen.blit(tank_sprite, self.tank_rect)
        
    def tank_collision_pos(self, center_tank, rotate=0):
        x0, y0 = center_tank
        # коорды position_local
        x1 = x0 - tank_width // 2
        y1 = y0 - tank_height // 2

        x2 = x0 + tank_width // 2
        y2 = y0 - tank_height // 2

        x3 = x0 - tank_width // 2
        y3 = y0 + tank_height // 2

        x4 = x0 + tank_width // 2
        y4 = y0 + tank_height // 2
        
        return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
