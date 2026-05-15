all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(WHITE, 20, 30)

sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")

bg_color = BLUE
screen.fill(bg_color)

running = False
exit = False

clock = pygame.time.Clock()

while not running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = True
            exit = True

        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()

        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            Sprite.change_background_color()

    all_sprites_list.update()

    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



