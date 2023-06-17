import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_TYPE

class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = PLAYER_TYPE
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0
    
    def update(self, game, user_input):
        self.shoot(game.bullet_manager, user_input)
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
    
    def move_left(self):
        self.rect.x -= 10
        if self.rect.x <= 0:
            self.rect.x = SCREEN_WIDTH - 55

    def move_right(self):
        self.rect.x +=10
        if self.rect.x >= SCREEN_WIDTH - 50:
            self.rect.x = 0
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -=10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y +=10
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager, user_input):
        if user_input[pygame.K_1]:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            
    def reset_position(self):
        self.rect.x = 520
        self.rect.y = 500
        
    def set_image(self, size=(40, 60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size) 