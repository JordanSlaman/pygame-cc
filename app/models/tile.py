from .enums import TileType, BootType
from .items.item import Item
from .items import Door, ChipGate, Box
from app.models.game.sprite import TILE_SPRITES


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
        elif self.type:
            return True

    def interact(self, player):
        slide_effect = self.type == TileType.SLIDE and not player.has_boots(BootType.SUCTION)
        ice_effect = self.type == TileType.ICE and not player.has_boots(BootType.SKATE)

        if slide_effect or ice_effect:
            player.lock_movement()
        else:
            player.unlock_movement()

        if self.item:
            self.item.interact(tile=self, player=player)
        elif slide_effect:
            player.interact_slide_spiral()
        elif ice_effect:
            player.interact_plain_ice()

    @property
    def sprite(self):
        if not self.item:
            if self.type == TileType.WALL:
                return TILE_SPRITES["wall"]
            elif self.type == TileType.WATER:
                return TILE_SPRITES["water"]
            elif self.type == TileType.SLIDE:
                return TILE_SPRITES["slide_spiral"]
            elif self.type == TileType.ICE:
                return TILE_SPRITES["ice"]
            else:
                return TILE_SPRITES["tile"]
        else:
            return self.item.sprite
