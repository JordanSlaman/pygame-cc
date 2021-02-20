from .sprite import TILE_SPRITES, tile_size

from .enums import Direction


class Player:

    def __init__(self, level, starting_tile):
        self.inventory = []
        self.chips_collected = 0

        self.level = level
        self.current_tile = starting_tile
        self.last_move = Direction.DOWN

    def move(self, direction: Direction):
        self.last_move = direction

        if direction == Direction.LEFT:
            destination_tile = self.level.get_tile(x_pos=self.x_pos - 1,
                                                   y_pos=self.y_pos)
        elif direction == Direction.RIGHT:
            destination_tile = self.level.get_tile(x_pos=self.x_pos + 1,
                                                   y_pos=self.y_pos)
        elif direction == Direction.UP:
            destination_tile = self.level.get_tile(x_pos=self.x_pos,
                                                   y_pos=self.y_pos - 1)
        else:
            destination_tile = self.level.get_tile(x_pos=self.x_pos,
                                                   y_pos=self.y_pos + 1)

        if destination_tile.is_navigable(self):
            self.current_tile = destination_tile
            self.current_tile.interact(self)

    def draw(self, window_surface):
        draw_pos = (self.x_pos * tile_size, self.y_pos * tile_size)
        window_surface.blit(self.sprite.surface, draw_pos)

    @property
    def x_pos(self):
        return self.current_tile.x_pos

    @property
    def y_pos(self):
        return self.current_tile.y_pos

    @property
    def sprite(self):
        if self.last_move == Direction.DOWN:
            return TILE_SPRITES["player_down"]
        if self.last_move == Direction.LEFT:
            return TILE_SPRITES["player_left"]
        if self.last_move == Direction.UP:
            return TILE_SPRITES["player_up"]
        if self.last_move == Direction.RIGHT:
            return TILE_SPRITES["player_right"]
