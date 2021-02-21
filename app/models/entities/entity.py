from app.models.enums import Direction
from app.models.game.sprite import tile_size
from app.models.tile import Tile


class Entity:

    def __init__(self, level, starting_tile: Tile, starting_direction: Direction = Direction.UP):

        self.level = level
        self.current_tile = starting_tile
        self.last_direction = starting_direction

    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.x_pos}, {self.y_pos})"

    @property
    def x_pos(self):
        return self.current_tile.x_pos

    @property
    def y_pos(self):
        return self.current_tile.y_pos

    @property
    def sprite(self):
        raise NotImplementedError

    @property
    def window_surface(self):
        return self.level.window_surface

    def draw(self):
        draw_pos = (self.x_pos * tile_size, self.y_pos * tile_size)
        self.window_surface.blit(self.sprite.surface, draw_pos)
