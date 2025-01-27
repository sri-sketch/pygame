
class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        # High score should never be reset,
        # and read highscore from the file.
        with open('highscore.csv') as file_object:
            self.high_score = file_object.read()
            self.high_score = int(self.high_score)
        self.reset_stats()
        self.level = 0

        # Start Alien Invasion game in in-active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize the statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
