from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BULLET_ICON

class MultishotPowerUp(PowerUp):
    def __init__(self):
        super().__init__(BULLET_ICON, "multishot")