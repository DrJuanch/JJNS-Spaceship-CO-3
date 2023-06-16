import pygame
from game.components.scores import Score
from game.utils.constants import FONT_STYLE, GAME_OVER, ICON, HALF_SCREEN_HEIGTH, HALF_SCREEN_WIDTH


class Menu:
    def __init__(self, message, text_size=30):
        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (HALF_SCREEN_WIDTH - 50, HALF_SCREEN_HEIGTH - 100)
        self.game_over = pygame.transform.scale(GAME_OVER, (650, 80))
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGTH - 100)
        self.update_message(message)
        self.score = Score()
    
    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()
    
    def draw_menu(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect.center)
        #actualiza la pantalla 
        pygame.display.update()
        
    def draw_menu_after_dead(self, screen):
        screen.fill((240, 240, 240))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.game_over, self.game_over_rect)
        self.score.draw_max_score(screen)
        self.score.draw_deaths(screen)
        pygame.display.update()
        
    def update_message(self, message):
        self.message = message
        #Este render recibe un str, byte, recibe la fuente y la renderiza en pantalla
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGTH)