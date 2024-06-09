import json
import os

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
        # Load the high score
        self.high_score = self.load_high_score()  # Load the high score

    def save_high_score(self, high_score):
        """Save the high score to a file."""
        with open('high_score.json', 'w') as f:
            json.dump(high_score, f)

    def load_high_score(self):
        """Load the high score from a file."""
        high_score = 0
        if os.path.exists('high_score.json'):
            with open('high_score.json', 'r') as f:
                high_score = json.load(f)
        return high_score

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Initialize stats
        self.ships_left = self.settings.ship_limit  # Number of ships left
        self.score = 0  # Current score
        self.level = 1  # Current level
