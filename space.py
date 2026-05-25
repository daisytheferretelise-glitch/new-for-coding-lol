import math
import random
import pygame

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40

PLAYER_WIDTH = 48
PLAYER_HEIGHT = 48
ENEMY_WIDTH = 48
ENEMY_HEIGHT = 48
COLLISION_DISTANCE = 35   # bigger so touching logo kills enemy

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo-clean.png")
pygame.display.set_icon(icon)

# clock
clock = pygame.time.Clock()

# background
background = pygame.image.load("space.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# -------------------------
# PLAYER (your cat)
# -------------------------
playerImg = pygame.image.load("player-cat.png")
playerImg = pygame.transform.scale(playerImg, (PLAYER_WIDTH, PLAYER_HEIGHT))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# -------------------------
# WEAPON (Ghostbusters logo)
# Always attached to player
# -------------------------
weaponImg = pygame.image.load("weapon.png")
weaponImg = pygame.transform.scale(weaponImg, (32, 32))

# enemy setup
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    img = pygame.image.load("enemy-clean.png")
    img = pygame.transform.scale(img, (ENEMY_WIDTH, ENEMY_HEIGHT))
    enemyImg.append(img)
    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score():
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 10))

def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def weapon(x, y):
    screen.blit(weaponImg, (x + 8, y - 5))  # sits on top of player

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance < COLLISION_DISTANCE

# game loop
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0

    # player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_WIDTH))

    # enemy movement + collision with weapon
    for i in range(num_of_enemies):

        # game over if enemy reaches bottom
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # collision with weapon (touch to kill)
        if isCollision(enemyX[i], enemyY[i], playerX, playerY):
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # draw player + weapon
    player(playerX, playerY)
    weapon(playerX, playerY)

    show_score()
    pygame.display.update()
    clock.tick(60)
