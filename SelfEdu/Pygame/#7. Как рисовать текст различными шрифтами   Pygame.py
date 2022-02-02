# import pygame
# pygame.init()
# print(pygame.font.get_fonts())
#
# f_sys = pygame.font.SysFont('arial', 12)
# f = pygame.font.Font('fonts/YandexSDLight.ttx', 24)

# ----------------------------------------------------------------------
#
# import pygame
# pygame.init()
#
# W, H = 600, 400
# sc = pygame.display.set_mode((600, 400))
# pygame.display.set_caption('Шрифты')
# pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))
#
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# YELLOW = (239, 228, 176)
#
# FPS = 60
# clock = pygame.time.Clock()
#
# f = pygame.font.SysFont('arial', 32)
# sc_text = f.render('Привет, мир!', True, RED, YELLOW)
# pos = sc_text.get_rect(center=(W//2, H//2))
#
# sc.fill(WHITE)
# sc.blit(sc_text, pos)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)

# -----------------------------------------------------------------------------

import pygame
pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Шрифты')
pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

FPS = 60
clock = pygame.time.Clock()

f = pygame.font.SysFont('arial', 32)
sc_text = f.render('Привет, мир!', True, RED, YELLOW)
pos = sc_text.get_rect(center=(W//2, H//2))


def draw_text():
    sc.fill(WHITE)
    sc.blit(sc_text, pos)
    pygame.display.update()

draw_text()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            pygame.mouse.get_rel() # Обнуляем первое смещение (при повторном вызове ниже)

        if pygame.mouse.get_focused() and pos.collidepoint(pygame.mouse.get_pos()):
            btns = pygame.mouse.get_pressed()
            if btns[0]:  # нажата левая кнопка мыши
                rel = pygame.mouse.get_rel()  # получаем смещение
                pos.move_ip(rel)
                draw_text()

    clock.tick(FPS)