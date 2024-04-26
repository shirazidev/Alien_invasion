import pygame

class Ship:
    
    # A manager for ship
    
    def __init__(self, ai_game):
        # initalize the ship and set start pos
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        
        #load ship image and get the shape
        
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        
        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # store a decimal value for the ship's horizental pos
        self.x = float(self.rect.x)
        
        # movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # update ship's pos based on the flag of movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # UPDATE RECT OBJ FROM SELF.X
        self.rect.x = self.x
        
    def blitme(self):
        # draw the ship at its current loc
        
        self.screen.blit(self.image, self.rect)