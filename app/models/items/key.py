from ..enums import Color
from ..sprite import TILE_SPRITES

from .item import Item


class Key(Item):

    def __init__(self, color: Color):
        self.color = color

    def __repr__(self):
        return f"{self.color.name} Key"

    def interact(self, tile, player):
        tile.item = None
        player.inventory.append(self)

    @property
    def sprite(self):
        if self.color == Color.RED:
            return TILE_SPRITES["key_red"]
        elif self.color == Color.BLUE:
            return TILE_SPRITES["key_blue"]
        elif self.color == Color.YELLOW:
            return TILE_SPRITES["key_yellow"]
        elif self.color == Color.GREEN:
            return TILE_SPRITES["key_green"]
