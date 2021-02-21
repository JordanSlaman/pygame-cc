from app.models.enums import BootType, Direction, IceCorner
from app.models.game.sprite import TILE_SPRITES

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

    def interact(self, tile, player):
        if not player.has_boots(BootType.SKATE):
            player.move_locked(direction=self.resolve_corner_direction(player))

    def resolve_corner_direction(self, player):
        try:
            return {
                # entering_from: {
                #    corner: resulting_direction
                # },
                Direction.LEFT: {
                    IceCorner.TOP_LEFT: Direction.DOWN,
                    IceCorner.BOTTOM_LEFT: Direction.UP,
                },
                Direction.DOWN: {
                    IceCorner.BOTTOM_LEFT: Direction.RIGHT,
                    IceCorner.BOTTOM_RIGHT: Direction.LEFT
                },
                Direction.RIGHT: {
                    IceCorner.TOP_RIGHT: Direction.DOWN,
                    IceCorner.BOTTOM_RIGHT: Direction.UP
                },
                Direction.UP: {
                    IceCorner.TOP_LEFT: Direction.RIGHT,
                    IceCorner.TOP_RIGHT: Direction.LEFT,
                }
            }[player.last_direction][self.corner]
        except KeyError:
            raise Exception("Map Error! - Entered Ice Bank Wrong...")
