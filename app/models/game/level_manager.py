import pygame


class LevelManager:

    def __init__(self, window_surface, key_handler):
        self.window_surface = window_surface
        self.key_handler = key_handler

        # Set attribute on key_handler for bi-directional referencing
        self.key_handler.level_manager = self
        self.key_handler.keys_locked = False

        # Must be imported after pygame display initialized
        from app.levels import Level1, Level2, Level3

        self.uninitialized_levels = {
            1: Level1,
            2: Level2,
            3: Level3,
        }

        self.set_level(level_id=1)

    @property
    def level(self):
        return self.current_level

    def initialize_all(self):
        self.initialized_levels = [l(manager=self) for l in self.uninitialized_levels.values()]

    def get_level_by_code(self, code: str):
        if not self.initialized_levels:
            self.initialize_all()
        for l in self.initialized_levels:
            if l.code == code:
                return l
        raise Exception(f"No Level: {code}")

    def incr_level(self):
        level_id = self.current_level.level_id + 1
        self.set_level(level_id)

    def re_initialize(self):
        self.set_level(self.current_level.level_id)

    def set_level(self, level_id):
        try:
            level = self.uninitialized_levels[level_id](manager=self)
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
