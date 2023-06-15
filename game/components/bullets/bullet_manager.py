import pygame
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE
from game.components.bullets.bullet import Bullet

class BulletManager:
    def __init__(self):
        self.player_bullets: list[Bullet]= []
        self.enemy_bullets: list[Bullet] = []
    
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
        
        #Verificar si hemos chocado con el jugador
        #coliderect recibe cómo parametro otra recta y dice si se encuentra con otra recta
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
        
        for player_bullet in self.player_bullets:
            player_bullet.update(self.player_bullets)
            
            for enemy in game.enemy_manager.enemies:
                if player_bullet.rect.colliderect(enemy):
                    self.player_bullets.remove(player_bullet)
                    game.enemy_manager.delete_enemy(enemy)
                    
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
        for bullet in self.player_bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        
        elif bullet.owner == PLAYER_TYPE:
            self.player_bullets.append(bullet)
            