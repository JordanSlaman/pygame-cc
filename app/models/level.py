from typing import List

from app.models.tile import Tile
from app.models.entities import Player
from app.models.items import *
from app.models.enums import BootType, Color, Direction, TileType, IceCorner
from app.models.sprite import tile_size


class Level:

    def __init__(self, manager, level_id: int, name: str, code: str, map_string: str):
        self.level_manager = manager

        self.level_id = level_id
        self.name = name
        self.code = code

        self.chip_count = 0
        self.player = None

        self.map = self.init_map(map_string)
        self.map_width = 0
        self.map_height = 0

        self.entities = []

    def __repr__(self):
        return f"Level {self.level_id}: {self.name}"

    def init_map(self, map_string):

        level_map = []
        map_lines = map_string.split('\n')
        map_lines[:] = [l for l in map_lines if l != ""]  # Strip blank lines

        self.map_height = len(map_lines)
        self.map_width = len(map_lines[0])
        self.display_size = (self.map_width * tile_size, self.map_height * tile_size)

        for y, line in enumerate(map_lines):
            if len(line) != self.map_width:
                raise Exception(f"Bad map string! non-uniform width on line: {y}")

            row = []
            for x, char in enumerate(line):
                row.append(self.create_tile(char=char, x_pos=x, y_pos=y))
            level_map.append(tuple(row))

        return tuple(level_map)

    def create_tile(self, char: str, x_pos: int, y_pos: int):
        if char == 'C':
            tile = Tile(x_pos=x_pos, y_pos=y_pos)
            self.player = Player(level=self, starting_tile=tile)
            return tile
        elif char == ' ':
            tile_kwargs = {}
        elif char == '#':
            tile_kwargs = {
                "tile_type": TileType.WALL
            }
        elif char == 'c':
            tile_kwargs = {
                "item": Chip(level=self)
            }
        elif char == '@':
            tile_kwargs = {
                "item": LevelExit(level=self)
            }
        elif char == 'X':
            tile_kwargs = {
                "item": ChipGate(level=self)
            }
        elif char == 'G':
            tile_kwargs = {
                "tile_type": TileType.WALL,
                "item": Door(color=Color.GREEN)
            }
        elif char == 'g':
            tile_kwargs = {
                "item": Key(color=Color.GREEN)
            }
        elif char == 'B':
            tile_kwargs = {
                "tile_type": TileType.WALL,
                "item": Door(color=Color.BLUE)
            }
        elif char == 'b':
            tile_kwargs = {
                "item": Key(color=Color.BLUE)
            }
        elif char == 'R':
            tile_kwargs = {
                "tile_type": TileType.WALL,
                "item": Door(color=Color.RED)
            }
        elif char == 'r':
            tile_kwargs = {
                "item": Key(color=Color.RED)
            }
        elif char == 'Y':
            tile_kwargs = {
                "tile_type": TileType.WALL,
                "item": Door(color=Color.YELLOW)
            }
        elif char == 'y':
            tile_kwargs = {
                "item": Key(color=Color.YELLOW)
            }
        elif char == 'w':
            tile_kwargs = {
                "tile_type": TileType.WATER
            }
        elif char == 'o':
            tile_kwargs = {
                "item": Box()
            }
        elif char == '{':
            tile_kwargs = {
                "item": Boots(type=BootType.FLIPPER)
            }
        elif char == '[':
            tile_kwargs = {
                "item": Boots(type=BootType.FIREPROOF)
            }
        elif char == '}':
            tile_kwargs = {
                "item": Boots(type=BootType.SKATE)
            }
        elif char == ']':
            tile_kwargs = {
                "item": Boots(type=BootType.SUCTION)
            }
        elif char == 's':
            tile_kwargs = {
                "tile_type": TileType.SLIDE
            }
        elif char == '<':
            tile_kwargs = {
                "tile_type": TileType.SLIDE,
                "item": SlideDirection(direction=Direction.LEFT)
            }
        elif char == '^':
            tile_kwargs = {
                "tile_type": TileType.SLIDE,
                "item": SlideDirection(direction=Direction.UP)
            }
        elif char == '>':
            tile_kwargs = {
                "tile_type": TileType.SLIDE,
                "item": SlideDirection(direction=Direction.RIGHT)
            }
        elif char == 'v':
            tile_kwargs = {
                "tile_type": TileType.SLIDE,
                "item": SlideDirection(direction=Direction.DOWN)
            }
        elif char == '_':
            tile_kwargs = {
                "tile_type": TileType.ICE
            }
        elif char == '`':
            tile_kwargs = {
                "tile_type": TileType.ICE,
                "item": IceBank(corner=IceCorner.TOP_LEFT)
            }
        elif char == '~':
            tile_kwargs = {
                "tile_type": TileType.ICE,
                "item": IceBank(corner=IceCorner.TOP_RIGHT)
            }
        elif char == ',':
            tile_kwargs = {
                "tile_type": TileType.ICE,
                "item": IceBank(corner=IceCorner.BOTTOM_RIGHT)
            }
        elif char == '.':
            tile_kwargs = {
                "tile_type": TileType.ICE,
                "item": IceBank(corner=IceCorner.BOTTOM_LEFT)
            }
        elif char == 'f':
            tile_kwargs = {
                "item": Fire()
            }
        elif char == 'i':
            tile_kwargs = {}  # Todo info item
        else:
            raise Exception(f"Bad map string! Unexpected char: {char}")

        return Tile(x_pos=x_pos, y_pos=y_pos, **tile_kwargs)

    def get_relative_tile(self, tile: Tile, direction: Direction):
        if direction == Direction.LEFT:
            return self.get_tile(x_pos=tile.x_pos - 1,
                                 y_pos=tile.y_pos)
        elif direction == Direction.UP:
            return self.get_tile(x_pos=tile.x_pos,
                                 y_pos=tile.y_pos - 1)
        elif direction == Direction.RIGHT:
            return self.get_tile(x_pos=tile.x_pos + 1,
                                 y_pos=tile.y_pos)
        elif direction == Direction.DOWN:
            return self.get_tile(x_pos=tile.x_pos,
                                 y_pos=tile.y_pos + 1)

    def get_tile(self, x_pos: int, y_pos: int):
        return self.map[y_pos][x_pos]

    def draw(self):
        for y_pos, row in enumerate(self.map):
            for x_pos, tile in enumerate(row):
                draw_pos = (x_pos * tile_size, y_pos * tile_size)
                self.window_surface.blit(tile.sprite.surface, draw_pos)

        self.player.draw()

        for e in self.entities:
            e.draw()

    def tick(self, time):
        for e in self.entities:
            e.tick(time)

    def create_path(self, start_x, start_y, direction_list):
        tile = self.get_tile(x_pos=start_x, y_pos=start_y)
        # (next_tile, last_direction)
        path = [(tile, direction_list[-1])]

        for direction in direction_list[:-1]:
            next_tile = self.get_relative_tile(tile=tile,
                                               direction=direction)
            path.append((next_tile, direction))
            tile = next_tile

        # Assert is a loop.
        start_tile, last_direction = path[0]
        last_tile = path[-1][0]
        if not self.get_relative_tile(last_tile, last_direction) == start_tile:
            raise Exception('Bad entity path! Does not loop!')

        return path

    @property
    def window_surface(self):
        return self.level_manager.window_surface