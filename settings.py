class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Light gray background

        # Ship settings
        self.ship_speed = 1.5  # Ship's speed
        self.ship_limit = 3  # Number of ships the player starts with

        # Bullet settings
        self.bullet_speed = 5.0  # Bullet's speed
        self.bullet_width = 3  # Bullet's width
        self.bullet_height = 15  # Bullet's height
        self.bullet_color = (60, 60, 60)  # Dark gray bullets
        self.bullets_allowed = 3  # Number of bullets allowed on screen at once

        # Alien settings
        self.alien_speed = 1.0  # Alien's speed
        self.fleet_drop_speed = 10  # Speed at which the fleet drops down the screen
        # fleet_direction of 1 represents moving right; -1 represents moving left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Initialize settings that change throughout the game
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5  # Initial ship speed
        self.bullet_speed = 3.0  # Initial bullet speed
        self.alien_speed = 1.0  # Initial alien speed

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50  # Points for each alien shot down

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale  # Increase ship speed
        self.bullet_speed *= self.speedup_scale  # Increase bullet speed
        self.alien_speed *= self.speedup_scale  # Increase alien speed

        # Increase points for each alien
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)  # Print new alien points for debugging
