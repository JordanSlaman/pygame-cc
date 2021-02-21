from enum import Enum


class TileType(Enum):
    FLOOR = 1
    WALL = 2
    WATER = 3
    SLIDE = 4
    ICE = 5


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
    EATEN = 3
    BURNED = 4


class BoxState(Enum):
    PUSHABLE = 1
    SUBMERGED = 2


class IceCorner(Enum):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4
