from ..enums import Color, TileType
from app.models.game.sprite import TILE_SPRITES
from .item import Item
from .key import Key


class Door(Item):

    def __init__(self, color: Color):
        self.color = color

    def is_navigable(self, player, tile):
        for inv_item in player.inventory:
            if isinstance(inv_item, Key) and inv_item.color == self.color:
                # Consumes a door & matching key
                player.inventory.remove(inv_item)
                print(f"You have used up a {self.color.name.title()} Key!")
                tile.item = None
                tile.type = TileType.FLOOR
                return True
        print(f"You cannot pass without a {self.color.name.title()} Key!")
        return False

    @property
    def sprite(self):
        if self.color == Color.RED:
            return TILE_SPRITES["door_red"]
        elif self.color == Color.BLUE:
            return TILE_SPRITES["door_blue"]
        elif self.color == Color.YELLOW:
            return TILE_SPRITES["door_yellow"]
        elif self.color == Color.GREEN:
            return TILE_SPRITES["door_green"]
