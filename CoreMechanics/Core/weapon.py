import pygame


class WeaponController:
    def __init__(self, pos):
        self.speed = 3
        self.pos = pos
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, "black", self.pos, 10)

    def bullet_move(self):
        self.pos.y -= self.speed
