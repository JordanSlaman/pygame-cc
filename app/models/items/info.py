from app.models.game.sprite import TILE_SPRITES

from .item import Item


class Info(Item):

    def __repr__(self):
        return "Info Tile!"

    def interact(self, tile, player):
        print(player.level.level_info)

    @property
    def sprite(self):
        return TILE_SPRITES["info"]
