from app.models.items import Boots

from app.models.enums import Direction, TileType, BootType, PlayerState
from app.models.game.sprite import TILE_SPRITES

from .entity import Entity


class Player(Entity):

    def __init__(self, level, starting_tile):
        super().__init__(level=level,
                         starting_tile=starting_tile,
                         starting_direction=Direction.DOWN)
        self.inventory = []
        self.chips_collected = 0

        self.state = PlayerState.ALIVE

        self.locked_move_speed_ms = 250
        self.locked_movement_timer = 0

    def move(self, direction: Direction):
        self.last_direction = direction

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
            }[self.last_direction]

        elif self.current_tile.type == TileType.WATER:
            if self.state == PlayerState.DROWNED:
                return TILE_SPRITES["player_drowned"]
            if self.state == PlayerState.BURNED:
                return TILE_SPRITES["player_burned"]
            return {
                Direction.DOWN: TILE_SPRITES["player_down_water"],
                Direction.LEFT: TILE_SPRITES["player_left_water"],
                Direction.UP: TILE_SPRITES["player_up_water"],
                Direction.RIGHT: TILE_SPRITES["player_right_water"]
            }[self.last_direction]

        elif self.current_tile.type == TileType.ICE:
            # todo: masking
            return {
                Direction.DOWN: TILE_SPRITES["player_down"],
                Direction.LEFT: TILE_SPRITES["player_left"],
                Direction.UP: TILE_SPRITES["player_up"],
                Direction.RIGHT: TILE_SPRITES["player_right"]
            }[self.last_direction]
        elif self.current_tile.type == TileType.SLIDE:
            # todo: masking
            return {
                Direction.DOWN: TILE_SPRITES["player_down"],
                Direction.LEFT: TILE_SPRITES["player_left"],
                Direction.UP: TILE_SPRITES["player_up"],
                Direction.RIGHT: TILE_SPRITES["player_right"]
            }[self.last_direction]
        return NotImplementedError('Unsupported Tile Type')

    def chips_remaining(self):
        return self.level.chip_count - self.chips_collected

    def has_boots(self, boot_type: BootType):
        for inv_item in self.inventory:
            if isinstance(inv_item, Boots) and inv_item.type == boot_type:
                return True
        return False

    def interact_slide_spiral(self):
        return NotImplementedError

    def interact_plain_ice(self):
        self.move_locked(direction=self.last_direction)

    def is_alive(self):
        return self.state == PlayerState.ALIVE

    def drown(self):
        self.state = PlayerState.DROWNED
        print(f"You drowned! Chip can't swim without flippers.")
        self.level_manager.re_initialize()

    def burn(self):
        self.state = PlayerState.BURNED
        print(f"You burned! Chip burned to a crisp!.")
        self.level_manager.re_initialize()

    def kill(self):
        self.state = PlayerState.EATEN
        print(f"You died! Chip was eaten by a bug.")
        self.level_manager.re_initialize()

    @property
    def level_manager(self):
        return self.level.level_manager

    @property
    def is_movement_locked(self):
        return self.level_manager.key_handler.keys_locked

    def lock_movement(self):
        self.level_manager.key_handler.keys_locked = True

    def unlock_movement(self):
        self.level_manager.key_handler.keys_locked = False

    def movement_locked_tick(self, time):
        # Game ticks at 60x/second.
        self.locked_movement_timer += time
        if self.locked_movement_timer > self.locked_move_speed_ms:
            self.locked_movement_timer = 0
            if not hasattr(self, "_locked_next_direction"):
                raise Exception("No Queued Direction!")
            self.move(direction=self._locked_next_direction)

    def move_locked(self, direction: Direction):
        self._locked_next_direction = direction