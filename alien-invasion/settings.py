class Settings:
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings.
        self.fleet_drop_speed = 10
        # How quickly the game speeds up.
        self.speed_up_scale = 1.1
        # How quickly the alien point value increases.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2.0
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represent left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed settings and alien point values."""
        self.ship_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)

