import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    #manage bullets that fired from ship
    
    def __init__(self, ai_game):
    # Create a bullet object at the ship's current location
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = ai_game.ship.rect.centerx  # Set bullet's x-coordinate to ship's center
        self.rect.midtop = ai_game.ship.rect.midtop  # Set bullet's y-coordinate to ship's top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        
    def update(self):
        #move bullet up to the screen
        # update decimal pos of bullet
        self.y -= self.settings.bullet_speed
        #update the rect pos
        self.rect.y = self.y
        
    def draw_bullet(self):
        #draw bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)