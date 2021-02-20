from app.models.items import Boots

from .sprite import TILE_SPRITES, tile_size
from .enums import Direction, TileType, BootType, PlayerState


class Player:

    def __init__(self, level, starting_tile):
        self.inventory = []
        self.chips_collected = 0

        self.level = level
        self.current_tile = starting_tile
        self.last_move = Direction.DOWN
        self.state = PlayerState.ALIVE

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

            if destination_tile.type == TileType.WATER and not self.has_boots(boot_type=BootType.FLIPPER):
                self.drown()

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
        if self.current_tile.type == TileType.FLOOR:
            if self.last_move == Direction.DOWN:
                return TILE_SPRITES["player_down"]
            elif self.last_move == Direction.LEFT:
                return TILE_SPRITES["player_left"]
            elif self.last_move == Direction.UP:
                return TILE_SPRITES["player_up"]
            elif self.last_move == Direction.RIGHT:
                return TILE_SPRITES["player_right"]

        elif self.current_tile.type == TileType.WATER:
            if self.state == PlayerState.DROWNED:
                return TILE_SPRITES["player_drowned"]
            elif self.last_move == Direction.DOWN:
                return TILE_SPRITES["player_down_water"]
            elif self.last_move == Direction.LEFT:
                return TILE_SPRITES["player_left_water"]
            elif self.last_move == Direction.UP:
                return TILE_SPRITES["player_up_water"]
            elif self.last_move == Direction.RIGHT:
                return TILE_SPRITES["player_right_water"]

    def has_boots(self, boot_type: BootType):
        for inv_item in self.inventory:
            if isinstance(inv_item, Boots) and inv_item.type == boot_type:
                return True
        return False

    def complete_level(self):
        print(f"Completed Level: {self.level.name}!")

    def drown(self):
        self.state = PlayerState.DROWNED
        print(f"You drowned! Chip can't swim without flippers.")
