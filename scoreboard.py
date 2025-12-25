import pygame
from asteroid import Asteroid
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class ScoreBoard():
    def __init__(self, font_name, size):
        self.font = pygame.font.SysFont(font_name, size)
        self.current_score = 0
        self.highest_score = 0

    def display_score(self, screen):
        score_surface = self._get_score_surface(f"Score: {self.current_score}")
        screen.blit(score_surface, (50, 50))

    def display_high_score(self, screen):
        score_surface = self._get_score_surface(f"High Score: {self.highest_score}")
        screen.blit(score_surface, (1100, 50))

    def increase_score(self, asteroid):
        if asteroid.radius == ASTEROID_MAX_RADIUS:
            self.current_score += 1
        elif asteroid.radius == ASTEROID_MIN_RADIUS:
            self.current_score += 5
        else:
            self.current_score += 3

    def _get_score_surface(self, text):
        return self.font.render(text, True, (255, 255, 255))
