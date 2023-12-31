import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE, SOUND_PATH
from game.components.bullets.bullet import Bullet


class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.speed = 10
        self.bullet_limit = 1

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game)

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right >= SCREEN_WIDTH - self.SPACESHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > self.HALF_SCREEN_HEIGHT:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)
        game.bullet_manager.set_bullet_limit(1)
        shot_sound = pygame.mixer.Sound(SOUND_PATH)
        shot_sound.play()

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.set_image()
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False

    def set_image(self, size = (40, 60), image = SPACESHIP):
        self.image = pygame.transform.scale(image, size)
