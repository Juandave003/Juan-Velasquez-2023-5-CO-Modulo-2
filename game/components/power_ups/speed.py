import pygame

from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPEED_ICON


class SpeedPowerUp(PowerUp):
    def __init__(self):
        super().__init__(SPEED_ICON, "speed")
