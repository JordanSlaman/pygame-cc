from app.models.enums import BootType
from app.models.sprite import TILE_SPRITES
from app.models.items.item import Item


class Fire(Item):

    @property
    def sprite(self):
        return TILE_SPRITES["fire"]

    def interact(self, tile, player):
        if not player.has_boots(BootType.FIREPROOF):
            player.burn()
