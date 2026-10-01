import pygame                      # bibliothèque pour faire des jeux (fenêtre, dessin, clavier)
import copy                        # permet de copier une liste d'objets sans les lier à l'original
import random                      # permet de tirer au hasard (pièces, couleurs)

width, height = 10, 20             # taille de la grille en cases : 10 colonnes, 20 lignes
tile = 35                          # taille d'une case en pixels
game_resolution = width * tile, height * tile   # taille en pixels de la zone de jeu (350 x 700)
resolution = 650, 780              # taille de la fenêtre complète
fps = 120                          # nombre maximum d'images par seconde

panel_x = (20 + game_resolution[0] + resolution[0]) // 2   # milieu horizontal du panneau de droite (entre la grille et le bord)
next_y = 250                                        # hauteur du centre de la pièce suivante

pygame.init()                                       # démarre pygame
sc = pygame.display.set_mode(resolution)            # crée la fenêtre principale
game_sc = pygame.Surface(game_resolution)           # crée une "feuille" séparée pour la zone de jeu
clock = pygame.time.Clock()                         # horloge pour limiter la vitesse du jeu

# liste de tous les rectangles de la grille (sert à dessiner le quadrillage)
grid = [pygame.Rect(x * tile, y * tile, tile, tile) for x in range(width) for y in range(height)]

# les 7 pièces : chaque pièce est une liste de 4 cases (x, y) relatives à un point de départ
figures_pos = [
                [(-1, 0), (-2, 0), (0, 0), (1, 0)],   # Ligne
                [(-1, 0), (-1, 1), (0, 0), (0, -1)],  # S gauche
                [(0, -1), (0, 0), (0, 1), (1, 1)],    # S droite
                [(0, 0), (0, 1), (1, 0), (1, 1)],     # Carré
                [(0, 1), (0, 0), (1, 0), (2, 0)],     # L gauche
                [(0, 0), (1, 0), (2, 0), (2, 1)],     # L droite
                [(0, 0), (1, 0), (1, 1), (2, 0)]      # T
                ]

# transforme chaque pièce en 4 rectangles 1x1 placés en haut au milieu de la grille
figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, tile, tile)         # rectangle réutilisé pour dessiner chaque case
field = [[0 for i in range(width)] for j in range(height)]   # grille des cases posées (0 = vide, sinon une couleur)

anim_count, anim_speed, anim_limit = 0, 60, 2000    # compteur de chute, vitesse de chute, seuil pour descendre d'une case

# chargement des images (chemins à adapter si tu changes d'ordinateur)
bg = pygame.image.load('C:/Users/victo/Documents/School/Projet Informatique/style/violet.png').convert()      # fond de la fenêtre
game_bg = pygame.image.load('C:/Users/victo/Documents/School/Projet Informatique/style/noir.jpg').convert()   # fond de la zone de jeu
bg = pygame.transform.scale(bg, resolution)             # CORRIGÉ : adapte le fond à la taille exacte de la fenêtre
game_bg = pygame.transform.scale(game_bg, game_resolution)   # CORRIGÉ : adapte le fond à la zone de jeu (image trop petite = traînées)

# chargement de la police d'écriture en deux tailles
main_font = pygame.font.Font('C:/Users/victo/Documents/School/Projet Informatique/style/font.ttf', 65)
font = pygame.font.Font('C:/Users/victo/Documents/School/Projet Informatique/style/font.ttf', 45)

# textes fixes, créés une seule fois
title_tetris = main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_score = font.render('score:', True, pygame.Color('green'))
title_record = font.render('record:', True, pygame.Color('pink'))

def random_color():                                 # renvoie une couleur au hasard
    return random.randrange(30, 220), random.randrange(30, 220), random.randrange(30, 220)   # (rouge, vert, bleu)

# pièce actuelle et pièce suivante, choisies au hasard (deepcopy = vraie copie)
figure, next_figure = copy.deepcopy(random.choice(figures)), copy.deepcopy(random.choice(figures))
color, next_color = random_color(), random_color()  # couleur de chaque pièce

score = 0                                           # score du joueur
lines = 0                                           # nombre de lignes complétées à cet instant
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}    # points gagnés selon le nombre de lignes d'un coup

def borders(i):                                     # vérifie si la case n°i de la pièce est dans un endroit interdit
    if figure[i].x < 0 or figure[i].x > width - 1:  # sort à gauche ou à droite de la grille ?
        return True
    if figure[i].y < 0 or figure[i].y > height - 1: # sort en haut ou en bas de la grille ? (CORRIGÉ : on testait pas le haut)
        return True
    if field[figure[i].y][figure[i].x]:             # la case est déjà occupée par un bloc posé ?
        return True
    return False                                    # sinon, tout va bien

def get_record():                                   # lit le record dans le fichier
    try:
        with open('record') as f:                   # ouvre le fichier 'record'
            return f.readline() or '0'              # renvoie sa première ligne (ou '0' si le fichier est vide)
    except FileNotFoundError:                       # si le fichier n'existe pas encore
        with open('record', 'w') as f:              # on le crée
            f.write('0')                            # avec un record de 0
        return '0'                                  # CORRIGÉ : avant, la fonction ne renvoyait rien -> plantage

def set_record(record, score):                      # enregistre le record si le score est meilleur
    rec = max(int(record), score)                   # garde le plus grand des deux
    with open('record', 'w') as f:                  # ouvre le fichier en écriture
        f.write(str(rec))                           # écrit le nouveau record

while True:                                         # boucle principale : une répétition = une image affichée
    record = get_record()                           # lit le record
    dx, rotate = 0, False                           # pas de déplacement ni de rotation par défaut
    sc.blit(bg, (0, 0))                             # dessine le fond violet sur la fenêtre
    game_sc.fill((0, 0, 0))                         # CORRIGÉ : efface tout en noir (plus aucune trace de l'image précédente)
    game_sc.blit(game_bg, (0, 0))                   # dessine le fond noir sur la zone de jeu

    for i in range(lines):                          # petite pause si des lignes viennent d'être faites
        pygame.time.wait(200)

    for event in pygame.event.get():                # parcourt tout ce que le joueur a fait (clavier, souris...)
        if event.type == pygame.QUIT:               # clic sur la croix de la fenêtre
            pygame.quit()                           # ferme pygame
            quit()                                  # arrête le programme
        if event.type == pygame.KEYDOWN:            # une touche vient d'être appuyée
            if event.key == pygame.K_LEFT:          # flèche gauche
                dx = -1                             # aller à gauche
            elif event.key == pygame.K_RIGHT:       # flèche droite
                dx = 1                              # aller à droite
            elif event.key == pygame.K_DOWN:        # flèche bas
                anim_limit = 30                     # chute rapide
            elif event.key == pygame.K_UP:          # flèche haut
                rotate = True                       # tourner la pièce

    # --- déplacement horizontal ---
    figure_old = copy.deepcopy(figure)              # sauvegarde la position avant de bouger
    for i in range(4):                              # pour chacune des 4 cases de la pièce
        figure[i].x += dx                           # on la décale
        if borders(i):                              # si ça tape un mur ou un bloc
            figure = copy.deepcopy(figure_old)      # on annule le mouvement
            break                                   # on arrête de vérifier

    # --- déplacement vertical (chute) ---
    anim_count += anim_speed                        # le compteur avance
    if anim_count > anim_limit:                     # assez de temps écoulé : on descend d'une case
        anim_count = 0                              # remet le compteur à zéro
        figure_old = copy.deepcopy(figure)          # sauvegarde la position avant de descendre
        for i in range(4):                          # pour chaque case de la pièce
            figure[i].y += 1                        # on la descend d'un cran
            if borders(i):                          # si on touche le fond ou un autre bloc
                for j in range(4):                  # on "colle" la pièce (à son ancienne position) dans la grille
                    field[figure_old[j].y][figure_old[j].x] = color
                figure = next_figure                # la pièce suivante devient la pièce actuelle
                color = next_color                  # idem pour la couleur
                next_figure = copy.deepcopy(random.choice(figures))   # nouvelle pièce suivante
                next_color = random_color()         # nouvelle couleur suivante
                anim_limit = 2000                   # vitesse de chute normale
                break                               # on arrête la boucle

    # --- rotation ---
    center = figure[0]                              # la première case sert de centre de rotation
    figure_old = copy.deepcopy(figure)              # sauvegarde avant de tourner
    if rotate:                                      # si le joueur a appuyé sur haut
        for i in range(4):                          # pour chaque case
            x = figure[i].y - center.y              # position relative au centre (calcul de rotation)
            y = figure[i].x - center.x
            figure[i].x = center.x - x              # nouvelle position après rotation de 90°
            figure[i].y = center.y + y
            if borders(i):                          # si la rotation est impossible
                figure = copy.deepcopy(figure_old)  # on annule
                break

    # --- vérification des lignes complètes ---
    line, lines = height - 1, 0                     # 'line' = ligne où on recopie, 'lines' = nombre de lignes complètes
    for row in range(height - 1, -1, -1):           # on parcourt la grille de bas en haut
        count = 0                                   # nombre de cases pleines dans cette ligne
        for i in range(width):                      # pour chaque colonne
            if field[row][i]:                       # si la case est pleine
                count += 1                          # on compte
            field[line][i] = field[row][i]          # on recopie la ligne vers 'line' (fait descendre les lignes)
        if count < width:                           # ligne incomplète : on la garde
            line -= 1                               # on passe à la ligne du dessus
        else:                                       # ligne complète : elle sera écrasée
            anim_speed += 3                         # le jeu accélère
            lines += 1                              # une ligne de plus

    score += scores[lines]                          # ajoute les points correspondants

    # --- dessin dans la zone de jeu (game_sc) ---
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]   # dessine le quadrillage gris

    for i in range(4):                              # dessine la pièce qui tombe
        figure_rect.x = figure[i].x * tile          # position en pixels = case * taille d'une case
        figure_rect.y = figure[i].y * tile
        pygame.draw.rect(game_sc, color, figure_rect)

    # CORRIGÉ : les blocs posés sont maintenant dessinés sur game_sc (avant ils allaient sur sc, sans le décalage de 20 px)
    for y, row in enumerate(field):                 # pour chaque ligne de la grille
        for x, col in enumerate(row):               # pour chaque case de la ligne
            if col:                                 # si la case contient un bloc posé
                figure_rect.x, figure_rect.y = x * tile, y * tile
                pygame.draw.rect(game_sc, col, figure_rect)   # on le dessine avec sa couleur

    # CORRIGÉ : on colle la zone de jeu sur la fenêtre APRÈS avoir tout dessiné dessus (avant : une image de retard)
    sc.blit(game_sc, (20, 20))

    # --- dessin de la pièce suivante (centrée dans le panneau de droite) ---
    xs = [r.x for r in next_figure]                 # toutes les colonnes occupées par la pièce suivante
    ys = [r.y for r in next_figure]                 # toutes les lignes occupées
    piece_w = (max(xs) - min(xs) + 1) * tile        # largeur de la pièce en pixels
    piece_h = (max(ys) - min(ys) + 1) * tile        # hauteur de la pièce en pixels
    start_x = panel_x - piece_w // 2 - min(xs) * tile   # point de départ pour que la pièce soit centrée en largeur
    start_y = next_y - piece_h // 2 - min(ys) * tile    # idem en hauteur
    for i in range(4):                              # dessine les 4 cases
        figure_rect.x = start_x + next_figure[i].x * tile
        figure_rect.y = start_y + next_figure[i].y * tile
        pygame.draw.rect(sc, next_color, figure_rect)

    # --- textes (tous centrés sur panel_x) ---
    sc.blit(title_tetris, title_tetris.get_rect(center=(panel_x, 60)))   # titre TETRIS
    sc.blit(title_score, title_score.get_rect(center=(panel_x, 470)))    # mot "score:"
    score_text = font.render(str(score), True, pygame.Color('white'))    # valeur du score (recréée à chaque image)
    sc.blit(score_text, score_text.get_rect(center=(panel_x, 530)))
    sc.blit(title_record, title_record.get_rect(center=(panel_x, 620)))  # mot "record:"
    record_text = font.render(record, True, pygame.Color('gold'))        # valeur du record
    sc.blit(record_text, record_text.get_rect(center=(panel_x, 680)))

    # --- game over : une case posée touche la ligne du haut ---
    for i in range(width):                          # on regarde la ligne 0 (tout en haut)
        if field[0][i]:                             # si une case y est occupée
            set_record(record, score)               # on sauvegarde le record
            field = [[0 for j in range(width)] for k in range(height)]   # on vide la grille
            anim_count, anim_speed, anim_limit = 0, 60, 2000             # on remet la vitesse de départ
            score = 0                               # le score repart à zéro
            for i_rect in grid:                     # petite animation : on remplit la grille de couleurs
                pygame.draw.rect(game_sc, random_color(), i_rect)
                sc.blit(game_sc, (20, 20))
                pygame.display.flip()               # affiche l'animation
                clock.tick(200)
            break                                   # CORRIGÉ : on sort de la boucle pour ne pas recommencer l'animation

    pygame.display.flip()                           # affiche l'image finale à l'écran
    clock.tick(fps)                                 # limite la vitesse à 'fps' images par seconde
