import math
import random
import pygame

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENIMIE_START_X_MIN=50
ENIMIE_START_Y_MAX=150
ENIMIE_START_X=4
ENIMIE_START_Y=40
BULLET_SPEED_Y=40

PLAYER_WIDTH=48
PLAYER_HEIGHT=48
ENIMIE_WIDTH=48
ENIMIE_HEIGHT=48
COLLISION_DISTANT=25

pygame.init()

SCREEN= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Space invaders")
ICON= pygame.image.load("evil inviader.jpg")
pygame.display.set_icon(ICON)
CLOCK=pygame.time.Clock()