import pygame
pygame.init()

W, H = 800, 600
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Изображения')
pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

FPS = 60
clock = pygame.time.Clock()

animal_surf = pygame.image.load('bober.png').convert_alpha() # - для изображений с прозрачным фном
bg_surf = pygame.image.load('sand.png').convert()
bg_surf = pygame.transform.scale(bg_surf, (W, H))


animal_up = animal_surf
animal_down = pygame.transform.flip(animal_surf, False, True)
animal_left = pygame.transform.rotate(animal_surf, 90)
animal_right = pygame.transform.rotate(animal_surf, -90)

animal_rect = animal_surf.get_rect(center=(W//2, H//2))
# animal_surf.set_colorkey((255, 255, 255)) # Обрезает белые края у изображения, если есть

animal = animal_up
speed = 5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        animal = animal_left
        animal_rect.x -= speed
        if animal_rect.x < 0:
            animal_rect.x = 0

    elif bt[pygame.K_RIGHT]:
        animal = animal_right
        animal_rect.x += speed
        if animal_rect.x > W - animal_rect.height:
            animal_rect.x = W - animal_rect.height

    elif bt[pygame.K_UP]:
        animal = animal_up
        animal_rect.y -= speed
        if animal_rect.y < 0:
            animal_rect.y = 0

    elif bt[pygame.K_DOWN]:
        animal = animal_down
        animal_rect.y += speed
        if animal_rect.y > H - animal_rect.height:
            animal_rect.y = H - animal_rect.height

    sc.blit(bg_surf, (0, 0))
    sc.blit(animal, animal_rect)
    pygame.display.update()
    clock.tick(FPS)

