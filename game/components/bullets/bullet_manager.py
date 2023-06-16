import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE

class BulletManager:
    def __init__(self):
        self.player_bullets: list[Bullet]= []
        self.enemy_bullets: list[Bullet] = []
    
    def update(self, game):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
        
        #Verificar si hemos chocado con el jugador
        #coliderect recibe cómo parametro otra recta y dice si se encuentra con otra recta
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                game.playing = False
                game.score.score_list.append(game.score.score)
                game.score.death_count += 1
                pygame.time.delay(1000)
                break
        
        for player_bullet in self.player_bullets:
            player_bullet.update(self.player_bullets)
            
            for enemy in game.enemy_manager.enemies:
                if player_bullet.rect.colliderect(enemy):
                    self.player_bullets.remove(player_bullet)
                    game.enemy_manager.delete_enemy(enemy)
                    game.score.score += 1
                    game.score.max_score += 1
                    game.score.score_list.append(game.score.max_score)
                    
    def draw(self, screen):
        all_bullets = self.enemy_bullets + self.player_bullets

        for bullet in all_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        
        elif bullet.owner == PLAYER_TYPE:
            self.player_bullets.append(bullet)
            