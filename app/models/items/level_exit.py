from .item import Item
from ..sprite import TILE_SPRITES


class LevelExit(Item):
    sprite = TILE_SPRITES['exit']

    def __init__(self, level):
        self.level = level

    def interact(self, tile, player):
        print(f'Completed Level: {self.level.name}!')
