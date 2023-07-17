import pygame
from CoreMechanics.Core.base_controller import BaseController


class PlayerController(BaseController):

    def __init__(self, pos, radius):
        super().__init__(pos, radius)

    def player_movement(self, player_pos, screen_pos):
        keys = pygame.key.get_pressed()
        if not player_pos.x < 0 and keys[pygame.K_a]:
            player_pos.x -= 300 * self.movement_speed
        if not player_pos.x > screen_pos and keys[pygame.K_d]:
            player_pos.x += 300 * self.movement_speed
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                temp_pos = player_pos.copy()
                self.shoot(temp_pos)
                self.last_shot = now
