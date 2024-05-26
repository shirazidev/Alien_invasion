


class GameStats:
    # track statistics for ai game
    def __init__(self, ai_game):
        # initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        # start ai in an active state
        self.game_active = False

    def reset_stats(self):
        # initialize stats that can change during game
        self.ships_left = self.settings.ship_limit

    # start alien invasion in an active state
