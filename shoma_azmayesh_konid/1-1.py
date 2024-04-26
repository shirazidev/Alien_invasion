import pygame
import sys

# this code is provided by shirazidve

class SkyWindow:
    """Class to create a sky-themed window."""
    def __init__(self):
        """Initialize the window."""
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (135, 206, 250)  # Sky blue color
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sky Window")

    def run(self):
        """Main loop for the window."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Check for events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update the screen."""
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    sky_window = SkyWindow()
    sky_window.run()
