import pygame
from constant import *


# класс танка
class Tank(object):
    def __init__(self, screen):
        self.screen = screen
        self.tank_time = 0
        self.tank_sprite = [pygame.image.load('assets/tank/Sprite-0001.png'),
                            pygame.image.load('assets/tank/Sprite-0002.png'),
                            pygame.image.load('assets/tank/Sprite-0003.png'),
                            pygame.image.load('assets/tank/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Sprite-0005.png')]

    def tank_stand(self, center_tank):
        self.tank_rect = self.tank_sprite[self.tank_time].get_rect(center=center_tank)
        self.screen.blit(self.tank_sprite[self.tank_time], self.tank_rect)

    def tank_drive(self, center_tank):
        self.tank_time = (self.tank_time + 1) % 5
        self.tank_rect = self.tank_sprite[self.tank_time].get_rect(center=center_tank)
        self.screen.blit(self.tank_sprite[self.tank_time], self.tank_rect)
