from app.models.enums import BootType
from app.models.game.sprite import TILE_SPRITES

from app.models.items.item import Item


class Boots(Item):

    def __init__(self, type: BootType):
        self.type = type

    def __repr__(self):
        return f"Boots: {self.type.name}"

    def interact(self, tile, player):
        tile.item = None
        player.inventory.append(self)

        if self.type == BootType.FLIPPER:
            print("You've collected flippers!")
        elif self.type == BootType.FIREPROOF:
            print("You've collected fireproof boots!")
        elif self.type == BootType.SKATE:
            print("You've collected skates!")
        elif self.type == BootType.SUCTION:
            print("You've collected suction boots!")


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
