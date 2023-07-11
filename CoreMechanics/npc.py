from CoreMechanics.Core.base_controller import BaseController


class NpcController(BaseController):
    def __init__(self):
        super().__init__()
        self.go_left = True
        self.go_right = False

    def npc_movement(self, npc_pos, screen_pos):
        if self.go_left:
            npc_pos.x -= 100 * self.movement_speed
            if npc_pos.x < 0:
                self.go_left = False
                self.go_right = True
        if self.go_right:
            npc_pos.x += 100 * self.movement_speed
            if npc_pos.x > screen_pos:
                self.go_left = True
                self.go_right = False

