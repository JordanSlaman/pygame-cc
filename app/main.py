import pygame

from app.models.enums import Direction
from app.utils.functions import one

from app.sprites.tile_map import tile_size


class ChipsChallenge:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 21 * tile_size, 14 * tile_size

        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Chip's Challenge")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        from app.levels import all_levels
        self.level = all_levels[1]
        self.level.draw(window_surface=self._display_surf)
        pygame.display.flip()

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:

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

    def on_loop(self):
        pass

    def on_render(self):

        self.level.draw(window_surface=self._display_surf)
        pygame.display.flip()

        # pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app = ChipsChallenge()
    app.on_execute()
