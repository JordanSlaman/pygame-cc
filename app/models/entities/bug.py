from app.models.enums import Direction
from app.models.game.sprite import TILE_SPRITES

from .pathed_entity import PathedEntity


class Bug(PathedEntity):

    @property
    def sprite(self):
        return {
            Direction.DOWN: TILE_SPRITES["bug_down"],
            Direction.LEFT: TILE_SPRITES["bug_left"],
            Direction.UP: TILE_SPRITES["bug_up"],
            Direction.RIGHT: TILE_SPRITES["bug_right"]
        }[self.last_direction]

    def player_collision(self):
        self.level.player.kill()
