# import pygame
#
# pygame.init()
#
# W = 600
# H = 400
#
# sc = pygame.display.set_mode((W, H))
# pygame.display.set_caption('События от мыши')
# pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))
#
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# FPS = 60
# clock = pygame.time.Clock()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print('Нажата кнопка: ', event.button)
#         elif event.type == pygame.MOUSEMOTION:
#             print('Позиция мыши: ', event.pos)
#             print('Изменение относительно прошлого положения: ', event.rel)
#     clock.tick(FPS)


# ----------------------------------------------------------------------------

# import pygame
#
# pygame.init()
#
# W = 600
# H = 400
#
# sc = pygame.display.set_mode((W, H))
# pygame.display.set_caption('События от мыши')
# pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))
#
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# FPS = 60
# clock = pygame.time.Clock()
#
# flStartDraw = False
# sp = ep = None
#
# sc.fill(WHITE)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             flStartDraw = True
#             sp = event.pos
#         elif event.type == pygame.MOUSEMOTION:
#             if flStartDraw:
#                 pos = event.pos
#
#                 width = pos[0] - sp[0]
#                 height = pos[1] - sp[1]
#
#                 sc.fill(WHITE)
#                 pygame.draw.rect(sc, BLUE, (sp[0], sp[1], width, height))
#                 pygame.display.update()
#         elif event.type == pygame.MOUSEBUTTONUP and event.button ==1:
#             flStartDraw = False
#
#     clock.tick(FPS)

# ---------------------------------------------------------------------------------
import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('События от мыши')
pygame.display.set_icon(pygame.image.load('icons8-кошка-50.png'))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

sp = None

sc.fill(WHITE)
pygame.display.update()

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(WHITE)
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(sc, BLUE, pos, 7)

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pos

        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
        sc.fill(WHITE)
        pygame.draw.rect(sc, BLUE, (sp[0], sp[1], width, height))

    else:
        sp = None
    pygame.display.update()

    clock.tick(FPS)
