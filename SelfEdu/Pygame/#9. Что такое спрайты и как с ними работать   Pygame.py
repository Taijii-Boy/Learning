import pygame
from ball import Ball

pygame.init()

W, H = 800, 600
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Спрайты')
pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

FPS = 60
clock = pygame.time.Clock()

speed = 1
b1 = Ball(W//2, 'icons8-бобер-30.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(BLACK)
    sc.blit(b1.image, b1.rect)
    pygame.display.update()

    clock.tick(FPS)

    if b1.rect.y < H - 30:
        b1.rect.y += speed
    else:
        b1.rect.y = 0
