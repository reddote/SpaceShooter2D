import pygame

from weapon import WeaponController


class PlayerController:
    def __init__(self):
        self.bullets = []
        self.movement_speed = 0.1

    def player_movement(self, player_pos, screen_pos):
        keys = pygame.key.get_pressed()
        if not player_pos.x < 0 and keys[pygame.K_a]:
            player_pos.x -= 300 * self.movement_speed
        if not player_pos.x > screen_pos and keys[pygame.K_d]:
            player_pos.x += 300 * self.movement_speed
        if keys[pygame.K_SPACE]:
            temp_pos = player_pos.copy()
            self.shoot(temp_pos)

    def shoot(self, pos):
        new_bullet = WeaponController(pos)
        self.bullets.append(new_bullet)
