import pygame


class WeaponController:
    def __init__(self, pos):
        self.speed = 3
        self.pos = pos
        self.bullet_radius = 10
        pass

    def draw(self, surface, rect):
        pygame.draw.circle(surface, "black", self.pos, self.bullet_radius)

        # Create a Rect with same center as the circle
        bullet_rect = pygame.Rect(0, 0, self.bullet_radius * 2, self.bullet_radius * 2)
        bullet_rect.center = (self.pos.x, self.pos.y)

        if bullet_rect.colliderect(rect):
            print("Collision Detected")

    def bullet_move(self):
        self.pos.y -= self.speed
