import pygame
import copy
import random

width, height = 10, 20
tile = 35
game_resolution = width * tile, height * tile
resolution = 650, 780
fps = 120

pygame.init()
sc = pygame.display.set_mode(resolution)
game_sc = pygame.Surface(game_resolution)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * tile, y * tile, tile, tile) for x in range(width) for y in range(height)]

figures_pos = [
                [(-1, 0), (-2, 0), (0, 0), (1, 0)],   # Ligne
                [(-1, 0), (-1, 1), (0, 0), (0, -1)],  # S gauche
                [(0, -1), (0, 0), (0, 1), (1, 1)],    # S droite
                [(0, 0), (0, 1), (1, 0), (1, 1)],     # Carré
                [(0, 1), (0, 0), (1, 0), (2, 0)],     # L gauche
                [(0, 0), (1, 0), (2, 0), (2, 1)],     # L droite
                [(0, 0), (1, 0), (1, 1), (2, 0)]      # T
                ]

figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, tile, tile)
field = [[0 for i in range(width)] for j in range(height)]

anim_count, anim_speed, anim_limit = 0, 60, 2000

bg = pygame.image.load('C:/Users/victo/Documents/School/Projet Informatique/style/violet.png').convert()
game_bg = pygame.image.load('C:/Users/victo/Documents/School/Projet Informatique/style/noir.jpg').convert()

main_font = pygame.font.Font('C:/Users/victo/Documents/School/Projet Informatique/style/font.ttf', 65)
font = pygame.font.Font('C:/Users/victo/Documents/School/Projet Informatique/style/font.ttf', 45)

title_tetris = main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_score = font.render('score:', True, pygame.Color('green'))
title_record = font.render('record:', True, pygame.Color('pink'))

def random_color():
    return random.randrange(30, 256), random.randrange(30, 256), random.randrange(30, 256)

figure, next_figure = copy.deepcopy(random.choice(figures)), copy.deepcopy(random.choice(figures))
color, next_color = random_color(), random_color()

score = 0
lines = 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

def borders():
    if figure[i].x < 0 or figure[i].x > width - 1:
        return True
    elif figure[i].y > height - 1 or field[figure[i].y][figure[i].x]:
        return True
    return False

def get_record():                       # A modifier avec la partie réseau
    try :
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')

def set_record(record, score):          # A modifier avec la partie réseau
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))

while True:
    record = get_record()
    dx, rotate = 0, False
    sc.blit(bg, (0,0))
    sc.blit(game_sc, (20, 20))
    game_sc.blit(game_bg, (0, 0))
    for i in range(lines):
        pygame.time.wait(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 30
            elif event.key == pygame.K_UP:
                rotate = True
    # bouger x
    figure_old = copy.deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if borders():
            figure = copy.deepcopy(figure_old)
            break

    # bouger y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = copy.deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if borders():
                for j in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure = next_figure
                color = next_color
                next_figure = copy.deepcopy(random.choice(figures))
                next_color = random_color()
                anim_limit = 2000
                break

    # rotation
    center = figure[0]
    figure_old = copy.deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if borders():
                figure = copy.deepcopy(figure_old)
                break

    # verif lignes
    line, lines = height - 1, 0
    for row in range(height - 1, -1, -1):
        count = 0
        for i in range(width):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < width:
            line -= 1
        else:
            anim_speed += 3
            lines += 1

    # score
    score += scores[lines]

    # dessiner la grille
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

    # dessiner la figure
    for i in range(4):
        figure_rect.x = figure[i].x * tile
        figure_rect.y = figure[i].y * tile
        pygame.draw.rect(game_sc, color, figure_rect)

    # dessiner le field
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col:
                figure_rect.x, figure_rect.y = x * tile, y * tile
                pygame.draw.rect(sc, col, figure_rect)

    # dessiner la figure suivante
    for i in range(4):
        figure_rect.x = next_figure[i].x * tile + 380
        figure_rect.y = next_figure[i].y * tile + 185
        pygame.draw.rect(sc, next_color, figure_rect)

    # dessiner les titres
    sc.blit(title_tetris, (485, -10))
    sc.blit(title_score, (535, 780))
    sc.blit(font.render(str(score), True, pygame.Color('white')), (550, 840))
    sc.blit(title_record, (525, 650))
    sc.blit(font.render(record, True, pygame.Color('gold')), (550, 710))
    # game over
    for i in range(width):
        if field[0][i]:
            set_record(record, score)
            field = [[0 for j in range(width)] for i in range(height)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            score = 0
            for i_rect in grid:
                pygame.draw.rect(game_sc, random_color(), i_rect)
                sc.blit(game_sc, (20, 20))
                pygame.display.flip()
                clock.tick(200)

    pygame.display.flip()
    clock.tick(fps)
