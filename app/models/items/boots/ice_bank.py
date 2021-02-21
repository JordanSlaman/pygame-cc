from app.models.enums import IceCorner
from app.models.sprite import TILE_SPRITES

from app.models.items.item import Item


class IceBank(Item):

    def __init__(self, corner: IceCorner):
        self.corner = corner

    @property
    def sprite(self):
        return {
            IceCorner.TOP_LEFT: TILE_SPRITES["ice_top_left"],
            IceCorner.TOP_RIGHT: TILE_SPRITES["ice_top_right"],
            IceCorner.BOTTOM_RIGHT: TILE_SPRITES["ice_bottom_right"],
            IceCorner.BOTTOM_LEFT: TILE_SPRITES["ice_bottom_left"],
        }[self.corner]
