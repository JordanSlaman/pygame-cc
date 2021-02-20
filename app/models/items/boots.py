from ..enums import BootType
from ..sprite import TILE_SPRITES

from .item import Item


class Boots(Item):

    def __init__(self, type: BootType):
        self.type = type

    def __repr__(self):
        return f"Boots: {self.type.name}"

    def interact(self, tile, player):
        tile.item = None
        player.inventory.append(self)

    @property
    def sprite(self):
        if self.type == BootType.FLIPPER:
            return TILE_SPRITES["boots_flipper"]
        elif self.type == BootType.FIREPROOF:
            return TILE_SPRITES["boots_fireproof"]
        elif self.type == BootType.SKATE:
            return TILE_SPRITES["boots_skate"]
        elif self.type == BootType.SUCTION:
            return TILE_SPRITES["boots_suction"]
