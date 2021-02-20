from enum import Enum


class TileType(Enum):
    FLOOR = 1
    WALL = 2


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Direction:
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
