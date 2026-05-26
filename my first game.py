import pygame

# initialize pygame
pygame.init()

# create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game Screen")

# background color (light blue)
background_color = (135, 206, 250)

# load an image (make sure the file is in the same folder)
# change "myimage.png" to your actual file name
image = pygame.image.load("myimage.png")
image_x = 300
image_y = 200

# title font
font = pygame.font.Font(None, 64)
title_text = font.render("My First Game Screen", True, (0, 0, 0))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill background
    screen.fill(background_color)

    # draw title text
    screen.blit(title_text, (180, 50))

    # draw image
    screen.blit(image, (image_x, image_y))

    # update display
    pygame.display.update()

pygame.quit()
