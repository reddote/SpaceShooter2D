import pygame
from CoreMechanics.Core.weapon import WeaponController


class BaseController:
    def __init__(self, pos, radius):
        self.movement_speed = 0.1
        self.bullets = []
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 500
        self.radius = radius
        self.pos = pos
        self.drawable_object_rect = pygame.Rect(0, 0, radius * 2, radius * 2)
        self.drawable_object_rect.center = (pos.x, pos.y)
        self.is_dead = False
        pass

    def draw(self, surface, color):
        if self.is_dead is False:
            drawable_object = pygame.draw.circle(surface, color, self.pos, self.radius)
            self.drawable_object_rect.center = (self.pos.x, self.pos.y)

    def shoot(self, pos):
        new_bullet = WeaponController(pos)
        self.bullets.append(new_bullet)

