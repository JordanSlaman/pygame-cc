import pygame

from app.models.enums import Direction
from app.models.level_manager import LevelManager
from app.utils.functions import one

from app.sprites.tile_map import tile_size

LEVEL_1_SIZE = 21 * tile_size, 14 * tile_size

class ChipsChallenge:
    def __init__(self):
        self._running = True
        self._display_surf = None

        self.clock = pygame.time.Clock()

        self.keys_locked = False
        self._key_repeat_timer = 0
        self._last_keydown_timer = 0
        self.last_keydown_timeout_ms = 250
        self.key_repeat_ms = 250

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Chip's Challenge")

        self._display_surf = pygame.display.set_mode(LEVEL_1_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.level_manager = LevelManager(window_surface=self._display_surf)
        self.level.draw()
        pygame.display.flip()

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            self._last_keydown_timer = 0
            self.handle_movement_keypress()

    def on_loop(self, time):
        self.level.tick(time)
        self.handle_key_repeat(time)

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

    def handle_key_repeat(self, time):
        self._key_repeat_timer += time
        self._last_keydown_timer += time

        if self._last_keydown_timer > self.key_repeat_ms and self._key_repeat_timer > self.key_repeat_ms:
            self._key_repeat_timer = 0
            self.handle_movement_keypress()

    def handle_movement_keypress(self):
        keystate = pygame.key.get_pressed()

        if one([keystate[pygame.K_RIGHT],
                keystate[pygame.K_LEFT],
                keystate[pygame.K_UP],
                keystate[pygame.K_DOWN]]):

            if keystate[pygame.K_RIGHT]:
                self.level.player.move(Direction.RIGHT)
            elif keystate[pygame.K_LEFT]:
                self.level.player.move(Direction.LEFT)
            elif keystate[pygame.K_UP]:
                self.level.player.move(Direction.UP)
            elif keystate[pygame.K_DOWN]:
                self.level.player.move(Direction.DOWN)

    @property
    def level(self):
        return self.level_manager.current_level


if __name__ == "__main__":
    app = ChipsChallenge()
    app.on_execute()
