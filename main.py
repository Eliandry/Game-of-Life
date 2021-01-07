import pygame
from copy import deepcopy

RES = WIDTH, HEIGHT = 1600, 900
TILE = 10
W, H = WIDTH // TILE, WIDTH // TILE
FPS = 10
pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next = [[0 for _ in range(W)] for _ in range(H)]
#current_field = [[1 if not (i*j)%34 else 0 for i in range(W)] for j in range(H)]
current_field = [[1 if not (i*2)%10 else 0 for i in range(W)] for j in range(H)]


def check(current, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1
    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count==3:
            return 1
        return 0

while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #[pygame.draw.line(surface, pygame.Color('#696969'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    #[pygame.draw.line(surface, pygame.Color('#696969'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    for x in range(1,W-1):
        for y in range(1,H-1):
            if current_field[y][x]:
                pygame.draw.rect(surface,pygame.Color('#778899'),(x*TILE+2,y*TILE+2,TILE-2,TILE+2))
            next[y][x]=check(current_field,x,y)

    current_field=deepcopy(next)
    pygame.display.flip()
    clock.tick(FPS)
