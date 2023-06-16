import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.game_over import GameOverMenu
from game.components.score_tracker import ScoreTracker


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.score_tracker = ScoreTracker()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.player = Spaceship(self.bullet_manager)
        self.menu = Menu('Press Any Key To Start...', self.screen)
        self.running = False
        self.game_over_menu = GameOverMenu('Game over. Press any key to restart', self.screen, self.score_tracker)
        self.game_over = False

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def show_game_over_menu(self):
        self.menu.reset(self.screen)
        game_over_menu = GameOverMenu('Game over. Press any key to restart', self.screen, self.score_tracker)
        game_over_menu.draw(self.screen)
        self.menu.update(self)

    def run(self):
        self.reset_game()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

            if not self.playing:
                self.show_game_over_menu()

        if self.game_over:
            self.show_game_over_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset(self.screen)

        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        icon = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))

        if self.score_tracker.death_count > 0:
            self.game_over_menu.draw(self.screen)
        else:
            self.menu.draw(self.screen)

        self.menu.update(self)


    def update_score(self):
        self.score_tracker.increase_score()
        self.score_tracker.update_highest_score()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score : {self.score_tracker.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def increase_death_count(self):
        self.score_tracker.increase_death_count()

    def reset_game(self):
        self.score_tracker.score = 0
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.player = Spaceship(self.bullet_manager)
        self.playing = False
