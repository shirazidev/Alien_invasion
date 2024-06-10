import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # Manage bullets fired from the ship

    def __init__(self, ai_game, x_offset=0, y_offset=0):
        # Create a bullet object at the ship's current location
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = ai_game.ship.rect.centerx + x_offset  # Set bullet's x-coordinate with offset
        self.rect.top = ai_game.ship.rect.top + y_offset  # Set bullet's y-coordinate with offset

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        # Move bullet up the screen
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)