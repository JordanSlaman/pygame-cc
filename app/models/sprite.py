from dataclasses import dataclass

import pygame
import pygame.locals

from ..sprites.tile_map import tiles, tile_size, tile_sprite_filepath


@dataclass
class Sprite:
    name: str
    surface: pygame.Surface
    height: int
    width: int

    def __repr__(self):
        return self.name


def init_tile_sprites():
    tile_sprites = {}
    tile_png = pygame.image.load(tile_sprite_filepath).convert()

    for name, pos in tiles.items():
        rect = pos + (tile_size,) * 2
        tile_sprites[name] = Sprite(name=name,
                                    surface=tile_png.subsurface(rect),
                                    height=tile_size,
                                    width=tile_size)
    return tile_sprites


TILE_SPRITES = init_tile_sprites()

# def init_ui_sprites():
#     pass
