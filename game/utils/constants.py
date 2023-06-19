import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
HALF_SCREEN_WIDTH = SCREEN_WIDTH //2
HALF_SCREEN_HEIGTH = SCREEN_HEIGHT //2
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
BULLET_TYPE = 'bullet'
LIFE_TYPE = 'life'
ENEMY_TYPE = "enemy"
PLAYER_TYPE = "player"
FASTER_ENEMY_TYPE = "faster enemy"
HEART_TYPE = "heart"

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
FASTER_ENEMY_BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_3.png"))

FONT_STYLE = 'freesansbold.ttf'

POWER_TIME = 500