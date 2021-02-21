import pygame


class LevelManager:

    def __init__(self, window_surface, key_handler):
        self.window_surface = window_surface
        self.key_handler = key_handler

        # Set attribute on key_handler for bi-directional referencing
        self.key_handler.level_manager = self
        self.key_handler.keys_locked = False

        # Must be imported after pygame display initialized
        from app.levels import levels

        self.levels_by_id = {l.level_id: l for l in levels}
        self.levels_by_code = {l.code: l for l in levels}

        print(self.levels_by_id)

        self.set_level_by_id(level_id=1)


    @property
    def level(self):
        return self.current_level

    def incr_level(self):
        level_id = self.current_level.level_id + 1
        self.set_level_by_id(level_id=level_id)

    def reinitialize(self):
        self.set_level_by_id(level_id=self.current_level.level_id)

    def set_level_by_code(self, code):
        try:
           level_id = self.levels_by_code[code]
           self.set_level_by_id(level_id)
        except KeyError:
            raise Exception(f"Incorrect Code: {code}")

    def set_level_by_id(self, level_id):
        try:
            level = self.levels_by_id[level_id](manager=self)
        except KeyError:
            raise Exception(f"No Level: {level_id}")

        self.current_level = level
        self.window_surface = pygame.display.set_mode(self.current_level.display_size,
                                                      pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.current_level.draw()

    def complete_level(self):
        print(f"Completed Level: {self.current_level.name}!")
        self.current_level.player.inventory = []
        self.incr_level()
