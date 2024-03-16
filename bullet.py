import pygame
from constant import *


# класс, отвечающий за снаряд и все с ним связанное
class Bullet(object):
    def __init__(self, center, game, tank_rotate, tank):
        self.bullet_img = pygame.image.load('assets/secondary objects/bullets/bullet.png')  # модель снаряда
        self.x, self.y = center
        self.game = game
        self.tank = tank
        self.tank_rotate = tank_rotate
        self.rotate = 0

        self.speed = -1  # скорость снаряда

    def fly(self):  # метод движения снаряда
        self.x, self.y = self.game.movement_1((self.x, self.y), self.speed, self.tank_rotate)

    def draw(self, screen):  # метод отрисовки снаряда
        bullet = self.bullet_img
        bull_rotate = pygame.transform.rotate(bullet, self.tank_rotate * delta)
        rect_bullet = bull_rotate.get_rect(center=self.game.grid_dict[(self.x, self.y)][0])

        screen.blit(bull_rotate, rect_bullet)

    def conflict(self):   # метод проверки столкновения снаряда со стеной
        pass
