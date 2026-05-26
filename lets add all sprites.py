import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Add Sprites")

# sprite positions
player_x, player_y = 100, 100
enemy_x, enemy_y = 500, 300
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed

    screen.fill((0, 0, 0))

    # player sprite
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 60, 60))

    # enemy sprite
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 60, 60))

    pygame.display.update()

pygame.quit()
