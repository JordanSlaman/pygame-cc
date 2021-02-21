import pygame


class LevelManager:

    def __init__(self, window_surface):
        self.window_surface = window_surface

        # Must be imported after pygame display initialized
        from app.levels import Level1, Level2, Level3

        self.levels = [l(manager=self) for l in (Level1, Level2, Level3)]
        self.current_level = self.levels[0]

    def get_level_by_code(self, code: str):
        for l in self.levels:
            if l.code == code:
                return l
        raise Exception(f"No Level: {code}")

    def get_level_by_id(self, level_id: int):
        for l in self.levels:
            if l.level_id == level_id:
                return l
        raise Exception(f"No Level: {level_id}")

    def incr_level(self):
        self.set_level(self.get_level_by_id(self.current_level.level_id + 1))

    def set_level(self, level):
        self.current_level = level
        self.window_surface = pygame.display.set_mode(self.current_level.display_size,
                                                      pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.current_level.draw()

    def complete_level(self):
        print(f"Completed Level: {self.current_level.name}!")
        self.current_level.player.inventory = []
        self.incr_level()
