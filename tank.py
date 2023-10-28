import pygame
from constant import *


# класс, отвечающий за анимации танка
class Tank(object):
    def __init__(self, screen):
        self.motion = 0  # вектор "движения"
        self.screen = screen
        self.tank_time = 0
        self.tank_sprite_straight = [pygame.image.load('assets/tank/Straight/Sprite-0001.png'),  # модель танка при движении вперёд/назад
                            pygame.image.load('assets/tank/Straight/Sprite-0002.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0003.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0005.png')]

        self.tank_sprite_right = [pygame.image.load('assets/tank/Straight/Sprite-0001.png'),  # модель танка при повороте направо
                            pygame.image.load('assets/tank/Turn right/Sprite-0006.png'),
                            pygame.image.load('assets/tank/Turn right/Sprite-0007.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Turn right/Sprite-0008.png'),
                            pygame.image.load('assets/tank/Turn right/Sprite-0009.png')]

        self.tank_sprite_left = [pygame.image.load('assets/tank/Straight/Sprite-0001.png'),  # модель танка при повороте налево
                            pygame.image.load('assets/tank/Turn left/Sprite-0010.png'),
                            pygame.image.load('assets/tank/Turn left/Sprite-0011.png'),
                            pygame.image.load('assets/tank/Straight/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Turn left/Sprite-0012.png'),
                            pygame.image.load('assets/tank/Turn left/Sprite-0013.png')]

    def tank_stand(self, center_tank, rotate):  # анимация танка, когда тот стоит
        rotate = rotate * 30

        tank_sprite = pygame.transform.rotate(self.tank_sprite_straight[self.tank_time], rotate)
        self.tank_rect = tank_sprite.get_rect(center=center_tank)
        self.screen.blit(tank_sprite, self.tank_rect)

    def tank_drive(self, center_tank, rotate, motion):  # анимация танка при движении
        rotate = rotate * 30
        sign = (motion > 0) - (motion < 0)

        self.tank_time = (self.tank_time + sign * 1) % 5
        tank_sprite = pygame.transform.rotate(self.tank_sprite_straight[self.tank_time], rotate)
        self.tank_rect = tank_sprite.get_rect(center=center_tank)
        self.screen.blit(tank_sprite, self.tank_rect)
        
    def tank_collision_pos(self, center_tank, rotate):
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
