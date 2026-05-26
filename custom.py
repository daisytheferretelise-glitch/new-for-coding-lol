import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Event Example")

# custom event every 1000 ms
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 1000)

# sprite positions
x1, y1 = 200, 250
x2, y2 = 500, 250

color1 = (255, 0, 0)
color2 = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill((20, 20, 20))

    pygame.draw.rect(screen, color1, (x1, y1, 80, 80))
    pygame.draw.rect(screen, color2, (x2, y2, 80, 80))

    pygame.display.update()

pygame.quit()
