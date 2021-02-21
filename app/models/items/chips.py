from .item import Item
from app.models.game.sprite import TILE_SPRITES


class Chip(Item):
    sprite = TILE_SPRITES["chip"]

    def __init__(self, level):
        level.chip_count += 1

    def __repr__(self):
        return self.__class__.__name__

    def interact(self, tile, player):
        tile.item = None
        player.chips_collected += 1
        print(f"You collected a chip! Remaining: {player.chips_remaining()}")


class ChipGate(Item):
    sprite = TILE_SPRITES["chip_gate"]

    def __init__(self, level):
        self.level = level
        self.chips_required = self.level.chip_count

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.chips_required}]"

    def is_navigable(self, player, tile):
        if player.chips_remaining() == 0:
            tile.item = None
            return True
        print("You cannot pass until you've collected all the chips!")
        return False
