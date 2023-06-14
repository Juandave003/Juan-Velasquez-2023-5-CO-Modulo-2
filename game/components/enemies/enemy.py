import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 1000]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    MOV_X = {0: 'left', 1: 'rigth'}

    def __init__(self, image, width, height, x_pos_list, y_pos, speed_x, speed_y, movement_x, move_x_for):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos_list[random.randint(0, 10)]
        self.rect.y = y_pos
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = movement_x
        self.move_x_for = move_x_for
        self.index = 0

    def update(self, ships):
        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0