import pygame
pygame.init()
window =pygame.display.set_mode((400,400))
window.fill ((255,255,255))
Pink=(225,192,203)
pygame.draw.circle(window,Pink,(100,200),50)
pygame.draw.circle(window,Pink,(300,300),50,3)
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()