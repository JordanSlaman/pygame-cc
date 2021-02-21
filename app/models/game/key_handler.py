import pygame

from app.models.enums import Direction
from app.utils.functions import one


class KeyHandler:

    def __init__(self):
        self.level_manager = None

        self.keys_locked = True
        self._key_repeat_timer = 0
        self._last_keydown_timer = 0
        self.last_keydown_timeout_ms = 250
        self.key_repeat_ms = 250

    @property
    def level(self):
        return self.level_manager.current_level

    def keydown_event(self):
        self._last_keydown_timer = 0
        keystate = pygame.key.get_pressed()
        self.handle_movement_keypress(keystate=keystate)
        self.handle_gamestate_keypress(keystate=keystate)

    def handle_key_repeat(self, time):
        self._key_repeat_timer += time
        self._last_keydown_timer += time

        if self._last_keydown_timer > self.key_repeat_ms and self._key_repeat_timer > self.key_repeat_ms:
            self._key_repeat_timer = 0
            keystate = pygame.key.get_pressed()
            self.handle_movement_keypress(keystate=keystate)

    def handle_movement_keypress(self, keystate):
        if self.keys_locked:
            return

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

    def handle_gamestate_keypress(self, keystate):

        if keystate[pygame.K_1]:
            self.level_manager.set_level(level_id=1)
        elif keystate[pygame.K_2]:
            self.level_manager.set_level(level_id=2)
        elif keystate[pygame.K_3]:
            self.level_manager.set_level(level_id=3)

        elif keystate[pygame.K_r]:
            self.level_manager.re_initialize()



