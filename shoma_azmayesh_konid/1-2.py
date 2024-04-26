import pygame
import sys

class Character:
    """Class to manage the character."""
    def __init__(self, screen):
        """Initialize the character."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)

class Game:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (135, 206, 250)  # Sky blue color
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Character Game")
        self.character = Character(self.screen)

    def run(self):
        """Start the main loop for the game."""
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
        self.character.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
