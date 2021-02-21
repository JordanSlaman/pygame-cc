from pathlib import Path

tile_sprite_filepath = Path('./sprites/tiles.png')
tile_size = 34

column = [0, 34, 68, 102, 136, 170, 204, 238]
row = [14, 48, 82, 116, 150, 184, 218, 252, 286, 320, 354, 388, 422, 456, 490, 524]

tiles = {

    "player_down": (column[0], row[0]),
    "player_left": (column[1], row[0]),
    "player_up": (column[2], row[0]),
    "player_right": (column[3], row[0]),

    "player_down_masked": (column[4], row[0]),
    "player_left_masked": (column[5], row[0]),
    "player_up_masked": (column[6], row[0]),
    "player_right_masked": (column[7], row[0]),

    "player_down_water": (column[0], row[1]),
    "player_left_water": (column[1], row[1]),
    "player_up_water": (column[2], row[1]),
    "player_right_water": (column[3], row[1]),

    "player_drowned": (column[4], row[1]),
    "player_burned": (column[5], row[1]),

    # "unused": (column[6], row[1]),
    # "unused": (column[7], row[1]),

    "key_red": (column[0], row[2]),
    "key_blue": (column[1], row[2]),
    "key_yellow": (column[2], row[2]),
    "key_green": (column[3], row[2]),

    "key_red_masked": (column[4], row[2]),
    "key_blue_masked": (column[5], row[2]),
    "key_green_masked": (column[6], row[2]),
    "key_yellow_masked": (column[7], row[2]),

    "boots_skate": (column[0], row[3]),
    "boots_suction": (column[1], row[3]),
    "boots_fireproof": (column[2], row[3]),
    "boots_flipper": (column[3], row[3]),

    "boots_skate_masked": (column[4], row[3]),
    "boots_suction_masked": (column[5], row[3]),
    "boots_fireproof_masked": (column[6], row[3]),
    "boots_flipper_masked": (column[7], row[3]),

    "bug_down": (column[0], row[4]),
    "bug_left": (column[1], row[4]),
    "bug_up": (column[2], row[4]),
    "bug_right": (column[3], row[4]),

    "bug_down_masked": (column[4], row[4]),
    "bug_left_masked": (column[5], row[4]),
    "bug_up_masked": (column[6], row[4]),
    "bug_right_masked": (column[7], row[4]),

    "tank_down": (column[0], row[5]),
    "tank_left": (column[1], row[5]),
    "tank_up": (column[2], row[5]),
    "tank_right": (column[3], row[5]),

    "tank_down_masked": (column[4], row[5]),
    "tank_left_masked": (column[5], row[5]),
    "tank_up_masked": (column[6], row[5]),
    "tank_right_masked": (column[7], row[5]),

    # ball row

    "ship_down": (column[0], row[7]),
    "ship_left": (column[1], row[7]),
    "ship_up": (column[2], row[7]),
    "ship_right": (column[3], row[7]),

    "ship_down_masked": (column[4], row[7]),
    "ship_left_masked": (column[5], row[7]),
    "ship_up_masked": (column[6], row[7]),
    "ship_right_masked": (column[7], row[7]),

    "alien_down": (column[0], row[8]),
    "alien_left": (column[1], row[8]),
    "alien_up": (column[2], row[8]),
    "alien_right": (column[3], row[8]),

    "alien_down_masked": (column[4], row[8]),
    "alien_left_masked": (column[5], row[8]),
    "alien_up_masked": (column[6], row[8]),
    "alien_right_masked": (column[7], row[8]),

    # amoeba row

    "tile": (column[0], row[10]),
    "chip": (column[1], row[10]),
    "chip_gate": (column[2], row[10]),

    # corner wall things

    "button_red": (column[0], row[11]),
    "button_blue": (column[1], row[11]),
    "button_green": (column[2], row[11]),
    "button_grey": (column[3], row[11]),
    "info": (column[4], row[11]),
    # emitters? Big buttons?

    "wall": (column[0], row[12]),
    # "wall_blue": (column[1], row[12]),
    # "wall_pretty": (column[3], row[12]),

    "door_red": (column[4], row[12]),
    "door_blue": (column[5], row[12]),
    "door_yellow": (column[6], row[12]),
    "door_green": (column[7], row[12]),

    "water": (column[0], row[13]),
    "ice": (column[1], row[13]),

    "box_pushable": (column[2], row[12]),
    "box_submerged": (column[2], row[13]),
    # "static": (column[3], row[13]),

    "ice_top_left": (column[4], row[13]),
    "ice_top_right": (column[5], row[13]),
    "ice_bottom_right": (column[6], row[13]),
    "ice_bottom_left": (column[7], row[13]),

    "slide_down": (column[0], row[14]),
    "slide_left": (column[1], row[14]),
    "slide_up": (column[2], row[14]),
    "slide_right": (column[3], row[14]),
    "slide_spiral": (column[4], row[14]),

    "fire": (column[5], row[14]),
    # "bomb": (column[6], row[14]),
    # "theif": (column[7], row[14]),

    # "magic_wall": (column[0], row[15]),
    # "magic_tile": (column[1], row[15]),
    "exit": (column[2], row[15]),
    # "unused": (column[3], row[15]),
    # "unused": (column[4], row[15]),
    # "blue": (column[7], row[15]),
}
