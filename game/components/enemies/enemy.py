from game.components.bullets.bullet import Bullet
import pygame
import random
from game.utils.constants import ENEMY_1, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.sprite import Sprite


LEFT = 'left'
RIGHT = 'right'
class Enemy(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST= [50, 100, 150, 200, 250, 300, 350, 400, 500, 550]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    
    def __init__(self):
        #Scale recibe un surface que es una imagen pero recibe cualquier parametro que se pueda renderizar en pantalla
        #scale(surface, (posicion x, posicion y))
        self.image = pygame.transform.scale(ENEMY_1, (50, 50) )
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        
        self.movement = random.choice(self.MOVEMENTS)
        #randint genera un número random entra los numeros dados (a, b)
        self.move_x = random.randint(30, 100)
        self.moving_index = 0
        self.shooting_time = random.randint(10, 20)
        
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else: 
            self.rect.x += self.speed_x
            
        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
        
    def update_movement(self):
        self.moving_index += 1
        if self.rect.x >= SCREEN_WIDTH -50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT
            
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT
            
            
    def draw(self, screen):
        #El metodo blit es igual al scale solo que uno transforma la imagen y blit lo renderiza, recibe los mismo parametros de la misma manera
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)