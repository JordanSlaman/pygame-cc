from app.models.enums import BootType, Direction
from app.models.game.sprite import TILE_SPRITES

from app.models.items.item import Item


class SlideDirection(Item):

    def __init__(self, direction: Direction):
        self.direction = direction

    @property
    def sprite(self):
        return {
            Direction.LEFT: TILE_SPRITES["slide_left"],
            Direction.UP: TILE_SPRITES["slide_up"],
            Direction.RIGHT: TILE_SPRITES["slide_right"],
            Direction.DOWN: TILE_SPRITES["slide_down"],
        }[self.direction]

    def interact(self, tile, player):
        if not player.has_boots(BootType.SUCTION):
            player.move_locked(direction=self.direction)
