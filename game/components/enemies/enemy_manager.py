from game.components.enemies.enemy import Enemy
from game.components.enemies.faster_enemy import FasterEnemy

class EnemyManager:
    def __init__(self):
        #Todo lo que está dentro de la lista serán objetos de la clase enemy
        self.enemies:list[Enemy] = []
        self.faster_enemies:list[FasterEnemy] = []
        
    def update(self, game):
        if not self.enemies or not self.faster_enemies:
            self.enemies.append(Enemy())
            self.faster_enemies.append(FasterEnemy())
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            
        for faster_enemy in self.faster_enemies:
            faster_enemy.update(self.faster_enemies)
    
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