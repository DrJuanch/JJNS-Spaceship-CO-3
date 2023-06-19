import pygame

from game.utils.constants import FONT_STYLE, HALF_SCREEN_HEIGTH, HALF_SCREEN_WIDTH


class Score:
    def __init__(self):
        self.score_list = [0]
        self.score = 0
        self.max_score = 0
        self.death_count = 0

    def draw_max_score(self, screen):
        max_score = max(self.score_list)
        second_position = HALF_SCREEN_HEIGTH + 100
        max_score_styles = self.styles(FONT_STYLE, 24, "Max score", max_score, HALF_SCREEN_WIDTH, second_position)
        screen.blit(max_score_styles[0], max_score_styles[1])
    
    def draw_deaths(self, screen):
        second_position = HALF_SCREEN_HEIGTH + 150
        death_styles = self.styles(FONT_STYLE, 18, "Deaths", self.death_count, HALF_SCREEN_WIDTH, second_position)
        screen.blit(death_styles[0], death_styles[1])
    
    def draw_score(self, screen):
        score_styles = self.styles(FONT_STYLE, 22, "score ", self.score, 1000, 50)
        screen.blit(score_styles[0], score_styles[1])
        
    def draw_life(self, screen, game):
        life_styles = self.styles(FONT_STYLE, 22, "life", game.player.life, 80, 50)
        screen.blit(life_styles[0], life_styles[1])

    def draw_power_up_time(self, screen, game):
        power_up_time = self.styles(FONT_STYLE, 22, "power_time", game.power_up_manager.time, 990, 550, (255, 255, 255))
        screen.blit(power_up_time[0], power_up_time[1])
    
    def styles(self, font_style, font_size, message, score, first_position, second_position, color = (255, 255, 255)):
        font = pygame.font.Font(font_style, font_size)
        text = font.render(f"{message}: {score}", True, (color))
        text_rect = text.get_rect()
        text_rect.center = (first_position, second_position)
        return (text, text_rect)

    def reset_all(self):
        self.max_score = 0
        self.score = 0
        