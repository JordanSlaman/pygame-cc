from .enums import TileType
from .items.item import Item
from .items import Door, ChipGate, Box
from .sprite import TILE_SPRITES


class Tile:

    def __init__(self, x_pos: int, y_pos: int, tile_type: TileType = TileType.FLOOR, item: Item = None):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.type = tile_type
        self.item = item

    def __repr__(self):
        return f"[{self.x_pos}, {self.y_pos}] - {self.type.name}: {self.item}"

    def is_navigable(self, player):
        if isinstance(self.item, (Door, ChipGate, Box)):
            return self.item.is_navigable(tile=self, player=player)
        elif self.type == TileType.WALL:
            return False
        elif self.type in (TileType.FLOOR, TileType.WATER):
            return True


    def interact(self, player):
        if self.item:
            self.item.interact(tile=self, player=player)

    @property
    def sprite(self):
        if not self.item:
            if self.type == TileType.WALL:
                return TILE_SPRITES["wall"]
            elif self.type == TileType.WATER:
                return TILE_SPRITES["water"]
            else:
                return TILE_SPRITES["tile"]
        else:
            return self.item.sprite
