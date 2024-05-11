import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # The class that operates a single alien

    def __init__(self, ai_game):
        # initalize alien and set start pos
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Alien Image and Its rect attribute
        self.image = pygame.image.load('img/ufo.png')
        self.rect = self.image.get_rect()

        # start each new alien near to left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's exact horizontal pos
        self.x = float(self.rect.x)


    def check_edges(self):
        # return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # move alien to right or left

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
