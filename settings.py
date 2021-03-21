class Settings:
    """A class to store all setting for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet directection  1 is to the right -1 is to the left
        self.fleet_direction = 1
