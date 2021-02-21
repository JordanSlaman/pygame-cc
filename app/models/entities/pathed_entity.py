from typing import List, Tuple

from app.models.enums import Direction
from app.models.tile import Tile

from .entity import Entity


class PathedEntity(Entity):

    def __init__(self,
                 level,
                 path: List[Tuple[Tile, Direction]],
                 path_starting_index: int = 0,
                 move_speed_ms: int = 500):
        self.path = path
        self.path_index = path_starting_index
        self.move_speed_ms = move_speed_ms

        starting_tile, starting_direction = self.path[self.path_index]
        super().__init__(level=level,
                         starting_tile=starting_tile,
                         starting_direction=starting_direction)

        self.timer = 0
        self.move_speed_ms = move_speed_ms

    def get_next_from_path(self):
        try:
            self.path_index += 1
            return self.path[self.path_index]
        except IndexError:
            self.path_index = 0
            return self.path[self.path_index]

    def path_move(self):
        next_tile, last_direction = self.get_next_from_path()

        self.current_tile = next_tile
        self.last_direction = last_direction

    def tick(self, time):
        # Game ticks at 60x/second.
        self.timer += time
        if self.timer > self.move_speed_ms:
            self.timer = 0
            self.path_move()

        player = self.level.player
        if self.current_tile == player.current_tile:
            self.player_collision()

    def player_collision(self):
        return NotImplementedError
