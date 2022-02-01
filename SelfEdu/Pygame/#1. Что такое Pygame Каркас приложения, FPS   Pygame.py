import pygame
pygame.init()

pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption('Моя игруля')
pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))

clock = pygame.time.Clock()
FPS = 60

# flRunning = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            # flRunning = False
            exit()

    # pygame.time.delay(20)  # Задержка на 20 мс - не учитывает время работы обработчика событий
    clock.tick(FPS)  # Учитывает время работы обработчиков событий
