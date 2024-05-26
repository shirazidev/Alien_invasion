class GameStats:
    """Track statistics for Alien Invasion game."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        # Get the game settings
        self.settings = ai_game.settings

        # Initialize stats
        self.reset_stats()

        # Start the game in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        # Initialize stats
        self.ships_left = self.settings.ship_limit  # Number of ships left
        self.score = 0  # Current score
        self.level = 1  # Current level

    # Start the game in an active state
