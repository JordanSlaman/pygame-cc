from app.models.items import Boots

from app.models.enums import Direction, TileType, BootType, PlayerState
from app.models.sprite import TILE_SPRITES

from .entity import Entity


class Player(Entity):

    def __init__(self, level, starting_tile):
        super().__init__(level=level,
                         starting_tile=starting_tile,
                         starting_direction=Direction.DOWN)
        self.inventory = []
        self.chips_collected = 0

        self.state = PlayerState.ALIVE

    def move(self, direction: Direction):
        self.last_move = direction

        destination_tile = self.level.get_relative_tile(tile=self.current_tile,
                                                        direction=direction)
        if destination_tile.is_navigable(self):
            self.current_tile = destination_tile

            if destination_tile.type == TileType.WATER and not self.has_boots(boot_type=BootType.FLIPPER):
                self.drown()

            self.current_tile.interact(self)

    @property
    def sprite(self):
        if self.current_tile.type == TileType.FLOOR:
            return {
                Direction.DOWN: TILE_SPRITES["player_down"],
                Direction.LEFT: TILE_SPRITES["player_left"],
                Direction.UP: TILE_SPRITES["player_up"],
                Direction.RIGHT: TILE_SPRITES["player_right"]
            }[self.last_move]

        elif self.current_tile.type == TileType.WATER:
            if self.state == PlayerState.DROWNED:
                return TILE_SPRITES["player_drowned"]
            return {
                Direction.DOWN: TILE_SPRITES["player_down_water"],
                Direction.LEFT: TILE_SPRITES["player_left_water"],
                Direction.UP: TILE_SPRITES["player_up_water"],
                Direction.RIGHT: TILE_SPRITES["player_right_water"]
            }[self.last_move]

    def has_boots(self, boot_type: BootType):
        for inv_item in self.inventory:
            if isinstance(inv_item, Boots) and inv_item.type == boot_type:
                return True
        return False

    def is_alive(self):
        return self.state == PlayerState.ALIVE

    def drown(self):
        self.state = PlayerState.DROWNED
        print(f"You drowned! Chip can't swim without flippers.")

    def burn(self):
        self.state = PlayerState.BURNED
        print(f"You burned! Chip burned to a crisp!.")

    def kill(self):
        self.state = PlayerState.EATEN
        print(f"You died! Chip was eaten by a bug.")
