from .item import Item
from ..sprite import TILE_SPRITES


class Chip(Item):
    sprite = TILE_SPRITES["chip"]

    def __init__(self, level):
        level.chip_count += 1

    def __repr__(self):
        return self.__class__.__name__

    def interact(self, tile, player):
        tile.item = None
        player.chips_collected += 1


class ChipGate(Item):
    sprite = TILE_SPRITES["chip_gate"]

    def __init__(self, level):
        self.level = level
        self.chips_required = self.level.chip_count

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.chips_required}]"

    def is_navigable(self, player, tile):
        if player.chips_collected == self.level.chip_count:
            tile.item = None
            return True
        return False
