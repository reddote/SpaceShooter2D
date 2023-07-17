import pygame


class WeaponController:
    def __init__(self, pos):
        self.speed = 3
        self.pos = pos
        self.bullet_radius = 10
        self.bullet_rect = None
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, "black", self.pos, self.bullet_radius)

        # Create a Rect with same center as the circle
        self.bullet_rect = pygame.Rect(0, 0, self.bullet_radius * 2, self.bullet_radius * 2)
        self.bullet_rect.center = (self.pos.x, self.pos.y)

    def bullet_move(self):
        self.pos.y -= self.speed
