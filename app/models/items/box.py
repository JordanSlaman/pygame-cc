from ..enums import BoxState, Direction, TileType
from ..sprite import TILE_SPRITES

from .item import Item


class Box(Item):

    def __init__(self, state: BoxState = BoxState.PUSHABLE):
        self.state = state

    def __repr__(self):
        return f"Box: {self.state.name}"

    def _tile_behind(self, tile, player):
        if player.last_move == Direction.LEFT:
            return player.level.get_tile(x_pos=tile.x_pos - 1,
                                         y_pos=tile.y_pos)
        elif player.last_move == Direction.UP:
            return player.level.get_tile(x_pos=tile.x_pos,
                                         y_pos=tile.y_pos - 1)
        elif player.last_move == Direction.RIGHT:
            return player.level.get_tile(x_pos=tile.x_pos + 1,
                                         y_pos=tile.y_pos)
        elif player.last_move == Direction.DOWN:
            return player.level.get_tile(x_pos=tile.x_pos,
                                         y_pos=tile.y_pos + 1)

    def is_navigable(self, tile, player):
        if self.state == BoxState.PUSHABLE:
            return self.can_push(tile=tile, player=player)
        elif self.state == BoxState.SUBMERGED:
            return True

    def can_push(self, tile, player):
        tile_behind = self._tile_behind(tile=tile, player=player)
        if tile_behind.is_navigable(player=player) and tile_behind.item is None:
            return True
        return False

    def interact(self, tile, player):
        if self.state == BoxState.SUBMERGED:
            tile.type = TileType.FLOOR
            tile.item = None
        elif self.state == BoxState.PUSHABLE:
            tile_behind = self._tile_behind(tile, player)
            if tile_behind.type == TileType.WATER:
                self.state = BoxState.SUBMERGED
            tile.item = None
            tile_behind.item = self

    @property
    def sprite(self):
        if self.state == BoxState.PUSHABLE:
            return TILE_SPRITES["box_pushable"]
        elif self.state == BoxState.SUBMERGED:
            return TILE_SPRITES["box_submerged"]
