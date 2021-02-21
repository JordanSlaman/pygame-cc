import pygame

from app.models.game.level_manager import LevelManager
from app.models.game.key_handler import KeyHandler

from app.sprites.tile_map import tile_size

LEVEL_1_SIZE = 21 * tile_size, 14 * tile_size

class ChipsChallenge:
    def __init__(self):
        self._running = True
        self._display_surf = None

        self.clock = pygame.time.Clock()
        self.key_handler = KeyHandler()

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Chip's Challenge")

        self._display_surf = pygame.display.set_mode(LEVEL_1_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.level_manager = LevelManager(window_surface=self._display_surf,
                                          key_handler=self.key_handler)
        self.level.draw()
        pygame.display.flip()

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            self.key_handler.keydown_event()

    def on_loop(self, time):
        self.level.tick(time)
        self.key_handler.handle_key_repeat(time)

    def on_render(self):
        self.level.draw()
        pygame.display.flip()

        # pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            time = self.clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop(time)
            self.on_render()
        self.on_cleanup()

    @property
    def level(self):
        return self.level_manager.current_level


if __name__ == "__main__":
    app = ChipsChallenge()
    app.on_execute()
