import sys
import pygame

# this code is provided by shirazidev

class Settings:
    """A class to store all settings for the game."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Missile settings
        self.missile_speed = 1.5

# this code is provided by shirazidev

class Missile:
    """A class to manage the missile."""
    def __init__(self, ai_game):
        """Initialize the missile and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the missile image and get its rect.
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        # Start each new missile at the center of the screen.
        self.rect.center = self.screen_rect.center

    # this code is provided by shirazidev

    def update(self):
        """Update the missile's position based on movement flags."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.settings.missile_speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.missile_speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.settings.missile_speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.missile_speed

    # this code is provided by shirazidev

    def blitme(self):
        """Draw the missile at its current location."""
        self.screen.blit(self.image, self.rect)

# this code is provided by shirazidev

class MissileGame:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Missile Game")
        self.missile = Missile(self)

    # this code is provided by shirazidev

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.missile.update()
            self._update_screen()

    # this code is provided by shirazidev

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    # this code is provided by shirazidev

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.missile.blitme()
        pygame.display.flip()

# this code is provided by shirazidev

if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = MissileGame()
    game.run_game()
