import sys as _sys

import pygame as _pygame


class PygameApp:
    FPS = 30

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
    def fps(self):
        return self.FPS

    def run(self):
        _pygame.init()
        screen = _pygame.display.set_mode(self.screen_size)
        clock = _pygame.time.Clock()
        dt = 0.0

        while True:
            for event in _pygame.event.get():
                if event.type == _pygame.QUIT:
                    _sys.exit()

                self.handle_event(event)

            self.update(dt)
            self.render(screen)
            _pygame.display.flip()
            dt = clock.tick(self.fps)
