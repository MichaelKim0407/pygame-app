import sys as _sys

import pygame as _pygame


class PygameApp:
    FPS = 30

    def __init__(self):
        self._screen: _pygame.surface.Surface = None
        self._clock: _pygame.time.Clock = None

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass

    @property
    def screen_size(self):
        raise NotImplementedError

    @property
    def desired_fps(self) -> int:
        return self.FPS

    @property
    def game_time(self) -> float:
        return _pygame.time.get_ticks() / 1000.0

    @property
    def actual_fps(self) -> float:
        return self._clock.get_fps()

    def run(self):
        _pygame.init()
        self._screen = _pygame.display.set_mode(self.screen_size)
        self._clock = _pygame.time.Clock()
        dt = 0.0

        while True:
            for event in _pygame.event.get():
                if event.type == _pygame.QUIT:
                    _sys.exit()

                self.handle_event(event)

            self.update(dt)
            self.render(self._screen)
            _pygame.display.flip()
            dt = self._clock.tick(self.desired_fps)
