class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()

        # load ferret image
        self.image = pygame.image.load("ferret.png").convert_alpha()

        # scale ferret to block size
        self.image = pygame.transform.scale(self.image, (width, height))

        # get rect
        self.rect = self.image.get_rect()

        # random velocity
        self.velocity = [
            random.choice([-1, 1]),
            random.choice([-1, 1])
        ]
