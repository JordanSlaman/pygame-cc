from .tile import Tile
from .player import Player
from .items import *
from .enums import Color, TileType
from .sprite import tile_size


class Level:

    def __init__(self, level_id: int, name: str, code: str, map_string=str):

        self.level_id = level_id
        self.name = name
        self.code = code

        self.chip_count = 0
        self.player = None

        self.map = self.init_map(map_string)
        self.map_width = 0
        self.map_height = 0

    def __repr__(self):
        return f"Level {self.level_id}: {self.name}"

    def init_map(self, map_string):

        level_map = []
        map_lines = map_string.split('\n')
        map_lines[:] = [l for l in map_lines if l != ""] # Strip blank lines


        self.map_height = len(map_lines)
        self.map_width = len(map_lines[0])

        for y, line in enumerate(map_lines):
            if len(line) != self.map_width:
                raise Exception(f"Bad map string! non-uniform width on line: {y}")

            row = []
            for x, char in enumerate(line):
                row.append(self.create_tile(char=char, x_pos=x, y_pos=y))
            level_map.append(tuple(row))

        return tuple(level_map)

    def create_tile(self, char: str, x_pos: int, y_pos: int):
        if char in (' '):
            return Tile(x_pos=x_pos, y_pos=y_pos)
        elif char == '#':
            return Tile(x_pos=x_pos, y_pos=y_pos, tile_type=TileType.WALL)
        elif char == 'c':
            return Tile(x_pos=x_pos, y_pos=y_pos, item=Chip(level=self))
        elif char == '@':
            return Tile(x_pos=x_pos, y_pos=y_pos, item=LevelExit(level=self))
        elif char == 'X':
            return Tile(x_pos=x_pos, y_pos=y_pos, item=ChipGate(level=self))
        elif char == 'G':
            return Tile(x_pos=x_pos, y_pos=y_pos, tile_type=TileType.WALL, item=Door(color=Color.GREEN))
        elif char == 'g':
            return Tile(x_pos=x_pos, y_pos=y_pos, item=Key(color=Color.GREEN))
        elif char == 'B':
            return Tile(x_pos=x_pos, y_pos=y_pos, tile_type=TileType.WALL, item=Door(color=Color.BLUE))
        elif char == 'b':
            return Tile(x_pos=x_pos, y_pos=y_pos, item=Key(color=Color.BLUE))
        elif char == 'R':
            return Tile(x_pos=x_pos, y_pos=y_pos, tile_type=TileType.WALL, item=Door(color=Color.RED))
        elif char == 'r':
            return Tile(x_pos=x_pos, y_pos=y_pos, item=Key(color=Color.RED))
        elif char == 'Y':
            return Tile(x_pos=x_pos, y_pos=y_pos, tile_type=TileType.WALL, item=Door(color=Color.YELLOW))
        elif char == 'y':
            return Tile(x_pos=x_pos, y_pos=y_pos, item=Key(color=Color.YELLOW))
        elif char == 'i':
            return Tile(x_pos=x_pos, y_pos=y_pos)  # Todo info item
        elif char == 'C':
            tile = Tile(x_pos=x_pos, y_pos=y_pos)
            self.player = Player(level=self, starting_tile=tile)
            return tile
        else:
            raise Exception(f"Bad map string! Unexpected char: {char}")

    def get_tile(self, x_pos: int, y_pos: int):
        selected = self.map[y_pos][x_pos]
        assert selected.x_pos == x_pos and selected.y_pos == y_pos
        return selected

    def draw(self, window_surface):

        for y_pos, row in enumerate(self.map):
            for x_pos, tile in enumerate(row):
                draw_pos = (x_pos * tile_size, y_pos * tile_size)
                window_surface.blit(tile.sprite.surface, draw_pos)

        self.player.draw(window_surface)