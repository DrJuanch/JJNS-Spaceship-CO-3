import pygame
import random
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.enemies.enemy import Enemy


UP = 'up'
DOWN = 'down'
class FasterEnemy(Enemy):
    MOVEMENTS = [UP, DOWN]
    X_POS_LIST= 20
    Y_POS = [50, 100, 150, 200, 250, 300, 350, 400, 500, 550, 600]
    SPEED_X = 5
    SPEED_Y = 5
    
    def __init__(self):
        #Scale recibe un surface que es una imagen pero recibe cualquier parametro que se pueda renderizar en pantalla
        #scale(surface, (posicion x, posicion y))
        self.image = pygame.transform.scale(ENEMY_2, (50, 50) )
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST
        self.rect.y = random.choice(self.Y_POS)
        self.type = ENEMY_TYPE
        
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        
        self.movement = random.choice(self.MOVEMENTS)
        #randint genera un número random entra los numeros dados (a, b)
        self.move_y = random.randint(10, 80)
        self.moving_index = 0
        
    def update(self, ships):
        self.rect.x += self.speed_x
        if self.movement == UP:
            self.rect.y -= self.speed_y
        else: 
            self.rect.y += self.speed_y
            
        self.update_movement()
        if self.rect.y >= SCREEN_WIDTH:
            ships.remove(self)
        
    def update_movement(self):
        self.moving_index += 1
        if self.rect.y >= SCREEN_HEIGHT - 50:
            self.movement = UP
        elif self.rect.y <= 0:
            self.movement = DOWN
            
        if self.moving_index >= self.move_y:
            self.moving_index = 0
            self.movement = UP if self.movement == DOWN else DOWN