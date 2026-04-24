import pygame
pygame.init()
grey =(128,128,128)

Clock =pygame.time.Clock()
display_surface=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Image")
image=pygame.image.load("my favorite.jpg")
Defualt_image_size=(150,150)
while True:
    display_surface.fill(grey)
    display_surface.blit(image,Defualt_image_size)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
    Clock.tick(30)