import pygame


class PlayerController:
    def __init__(self):
        pass

    def player_movement(self, player_pos, screen_pos):
        movement_speed = 0.1

        keys = pygame.key.get_pressed()
        if not player_pos.x < 0 and keys[pygame.K_a]:
            player_pos.x -= 300 * movement_speed
        if not player_pos.x > screen_pos and keys[pygame.K_d]:
            player_pos.x += 300 * movement_speed
