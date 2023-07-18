import pygame

from CoreMechanics.Core.base_controller import BaseController


class NpcController(BaseController):
    def __init__(self, pos, radius):
        super().__init__(pos, radius)
        self.go_left = True
        self.go_right = False
        # Store the starting x position
        self.temp_pos = pos.x

    def npc_movement(self, npc_pos, screen_pos):
        new_pos = pygame.Vector2(npc_pos)
        if self.go_left:
            new_pos.x -= 100 * self.movement_speed
            print(new_pos.x - self.temp_pos)
            if new_pos.x - self.temp_pos < -300:
                self.go_left = False
                self.go_right = True
        if self.go_right:
            new_pos.x += 100 * self.movement_speed
            if new_pos.x - self.temp_pos > 300:
                self.go_left = True
                self.go_right = False
        return new_pos
