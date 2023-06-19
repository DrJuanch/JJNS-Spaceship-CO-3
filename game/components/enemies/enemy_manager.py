import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.faster_enemy import FasterEnemy

class EnemyManager:
    def __init__(self):
        #Todo lo que está dentro de la lista serán objetos de la clase enemy
        self.enemies:list[Enemy] = []
        self.faster_enemies:list[FasterEnemy] = []
        self.enemy_timer = 0
        self.faster_enemy_timer = 0
        self.enemy_appears = 5000
        self.faster_enemy_appears = 9000
        
        
    def update(self, game):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.enemy_timer >= self.enemy_appears:
            self.enemies.append(Enemy())
            self.enemy_timer = current_time
            
        if current_time - self.faster_enemy_timer >= self.faster_enemy_appears:
            self.faster_enemies.append(FasterEnemy())
            self.faster_enemy_timer = current_time
            
        for faster_enemy in self.faster_enemies:
            faster_enemy.update(self.faster_enemies, game)

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        
        for faster_enemy in self.faster_enemies:
            faster_enemy.draw(screen)
            
    def delete_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
        
        elif enemy in self.faster_enemies:
            self.faster_enemies.remove(enemy)
            
    def reset(self):
        self.enemies.clear()
        self.faster_enemies.clear()