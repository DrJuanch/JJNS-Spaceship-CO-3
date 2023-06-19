import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, FASTER_ENEMY_TYPE, PLAYER_TYPE, SHIELD_TYPE

class BulletManager:
    def __init__(self):
        self.player_bullets: list[Bullet]= []
        self.enemy_bullets: list[Bullet] = []
        self.faster_enemy_bullets: list[Bullet] = []
    
    def update(self, game):
        for faster_enemy_bullet in self.faster_enemy_bullets:
            faster_enemy_bullet.update(self.faster_enemy_bullets)
            
            if faster_enemy_bullet.rect.colliderect(game.player.rect):
                self.faster_enemy_bullets.remove(faster_enemy_bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.life -= 50
                
                if game.player.life <= 0:
                    game.playing = False
                    game.menu.score.death_count += 1
                    game.player.reset()
                    self.reset_bullets()
                    game.menu.score.reset_all()
                    game.menu.score.score_list.append(game.menu.score.max_score)
                    pygame.time.delay(1500)
                    
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
        
        #Verificar si hemos chocado con el jugador
        #coliderect recibe cómo parametro otra recta y dice si se encuentra con otra recta
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.life -= 20
                
                if game.player.life <= 0:
                    game.playing = False
                    game.menu.score.death_count += 1
                    game.player.reset()
                    self.reset_bullets()
                    game.menu.score.reset_all()
                    game.menu.score.score_list.append(game.menu.score.max_score)
                    pygame.time.delay(1500)
                
        for player_bullet in self.player_bullets:
            player_bullet.update(self.player_bullets)
            
            for enemy in game.enemy_manager.enemies:
                if player_bullet.rect.colliderect(enemy):
                    self.player_bullets.remove(player_bullet)
                    game.enemy_manager.delete_enemy(enemy)
                    game.menu.score.score += 1
                    game.menu.score.max_score += 1
            
            for faster_enemy in game.enemy_manager.faster_enemies:
                if player_bullet.rect.colliderect(faster_enemy):
                    self.player_bullets.remove(player_bullet)
                    game.enemy_manager.delete_enemy(faster_enemy)
                    game.menu.score.score += 1
                    game.menu.score.max_score += 1
                    
    def draw(self, screen):
        all_bullets = self.enemy_bullets + self.player_bullets + self.faster_enemy_bullets

        for bullet in all_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        
        elif bullet.owner == PLAYER_TYPE:
            self.player_bullets.append(bullet)
            
        elif bullet.owner == FASTER_ENEMY_TYPE and not self.faster_enemy_bullets:
            self.faster_enemy_bullets.append(bullet)
    
    def reset_bullets(self):
        self.enemy_bullets.clear()
        self.player_bullets.clear()
        self.faster_enemy_bullets.clear()