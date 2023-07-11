import pygame
from CoreMechanics.Core.weapon import WeaponController


class BaseController:
    def __init__(self):
        self.movement_speed = 0.1
        self.bullets = []
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 500
        pass

    def shoot(self, pos):
        new_bullet = WeaponController(pos)
        self.bullets.append(new_bullet)
