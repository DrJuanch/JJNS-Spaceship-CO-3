from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        #Todo lo que está dentro de la lista serán objetos de la clase enemy
        self.enemies:list[Enemy] = []
    
    def update(self):
        if not self.enemies:
            self.enemies.append(Enemy())
            
        for enemy in self.enemies:
            enemy.update(self.enemies)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)