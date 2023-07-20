import random

import pygame

from CoreMechanics.Core.base_controller import BaseController


class NpcController(BaseController):
    def __init__(self, pos, radius):
        super().__init__(pos, radius)
        self.go_left = True
        self.go_right = False
        # Store the starting x position
        self.temp_pos = pos.x
        self.shoot_delay = 1000

    def npc_movement(self, npc_pos):
        new_pos = pygame.Vector2(npc_pos)
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            temp_pos = npc_pos.copy()
            self.shoot(temp_pos)
            self.last_shot = now
        if self.go_left:
            new_pos.x -= 100 * self.movement_speed
            # print(new_pos.x - self.temp_pos)
            if new_pos.x - self.temp_pos < -300:
                self.go_left = False
                self.go_right = True
        if self.go_right:
            new_pos.x += 100 * self.movement_speed
            if new_pos.x - self.temp_pos > 300:
                self.go_left = True
                self.go_right = False
        return new_pos



