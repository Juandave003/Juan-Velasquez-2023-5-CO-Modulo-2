import pygame
from game.utils.constants import FONT_STYLE
from game.components.menu import Menu

class GameOverMenu(Menu):
    def __init__(self, message, screen, score_tracker):
        super().__init__(message, screen)
        self.score_tracker = score_tracker

    def draw(self, screen):
        super().draw(screen)
        self.draw_score(screen)

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)

        score_text = font.render(f"Your score: {self.score_tracker.score}", True, (0, 0, 0))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)
        screen.blit(score_text, score_text_rect)

        highest_score_text = font.render(f"Highest score: {self.score_tracker.highest_score}", True, (0, 0, 0))
        highest_score_text_rect = highest_score_text.get_rect()
        highest_score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        screen.blit(highest_score_text, highest_score_text_rect)

        death_count_text = font.render(f"Total deaths: {self.score_tracker.death_count}", True, (0, 0, 0))
        death_count_text_rect = death_count_text.get_rect()
        death_count_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
        screen.blit(death_count_text, death_count_text_rect)
