import random

import pygame
from game.components.powerups.heart import Heart
from game.components.powerups.power_up import PowerUp

from game.components.powerups.shield import Shield
from game.utils.constants import DEFAULT_TYPE, HEART_TYPE, POWER_TIME, SHIELD_TYPE, SPACESHIP_SHIELD


class Manager:
    def __init__(self):
        self.power_ups:list[PowerUp] = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = random.randint(3,5)
        self.time = POWER_TIME
        
    def generate_power(self):
        shield = Shield()
        heart = Heart()
        power_generator = [shield, heart]
        power_selector = random.choice(power_generator)
        self.when_appears += random.randint(10000,15000)
        self.power_ups.append(power_selector)
        
    def update(self, game):
        current_time = pygame.time.get_ticks()
        
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power()
        
        elif game.player.has_power_up:
            self.time -= 1
            if self.time <= 0:
                game.player.set_image()
                self.time = 500
                game.player.has_power_up = False
                game.player.power_up_type = DEFAULT_TYPE
                
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                if power_up.type == SHIELD_TYPE:        
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_up_time = power_up.start_time + (self.duration*1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
                    
                elif power_up.type == HEART_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.life += 30
                    print(game.player.life)
                    self.power_ups.remove(power_up)
                    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears_power = random.randint(now + 10000, now + 15000)
        self.time = 500