from enum import Enum


class TileType(Enum):
    FLOOR = 1
    WALL = 2
    WATER = 3


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class BootType(Enum):
    FLIPPER = 1
    SKATE = 2
    SUCTION = 3
    FIREPROOF = 4


class PlayerState(Enum):
    ALIVE = 1
    DROWNED = 2
    BURNED = 3

class BoxState(Enum):
    PUSHABLE = 1
    SUBMERGED = 2