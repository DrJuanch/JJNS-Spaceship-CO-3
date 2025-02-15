from game.components.powerups.manager import Manager
from game.components.menu import Menu
from game.components.bullets.bullet_manager import BulletManager
import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.spaceship import Spaceship
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        
        
        
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = Manager()
        self.menu = Menu("Press any key to start...")
        
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.enemy_manager.reset()
        self.playing = True
        self.menu.score.score
        
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(self, user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.menu.score.draw_score(self.screen)
        self.menu.score.draw_life(self.screen, self)
        self.menu.score.draw_power_up_time(self.screen, self)
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))# blit dibuja lo que queremos en la posición que queremos 
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def show_menu(self):
        if self.menu.score.death_count > 0:
            self.menu.update_message("Press any key to play again...")
            self.draw_background()
            self.menu.draw_menu_after_dead(self.screen)
        else:
            self.draw_background()
            self.menu.draw_menu(self.screen)
        
        self.menu.events(self.on_close, self.play)
        
    def on_close(self):
        self.playing = False
        self.running = False