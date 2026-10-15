import random

width = 10
height = 20

figures = [
    [(1, 0), (0, 0),  (2, 0), (3, 0)],   # 0 : la barre (I)
    [(0, 1), (0, 2),  (1, 1), (1, 0)],  # 1 : S
    [(0, 1), (0, 0), (1, 1), (1, 2)],    # 2 : Z
    [(0, 0), (0, 1), (1, 0), (1, 1)],     # 3 : le carré (O)
    [(1, 0), (0, 1), (0, 0), (2, 0)],     # 4 : L
    [(1, 0), (0, 0), (2, 0), (2, 1)],     # 5 : J
    [(1, 0), (0, 0), (1, 1), (2, 0)],     # 6 : T
]

# Vitesses en millisecondes du jeu
fallSpeed = 1000
fastFallSpeed = 50

#Jeu solo
class Tetris:

    # Le __init__ est la première méthode éxécutée lors de la création d'une partie
    # On y crée toutes les choses nécessaires pour la partie
    def __init__(self):
        self.board = []
        for y in range(height):
            line = []
            for x in range(width):
                line.append(0)              # Une case vide vaut 0, choix de logique
            self.board.append(line)

        self.score = 0
        self.gameOver = False

        self.fallSpeed = fallSpeed
        self.time = 0

        self.currentFigure = random.randint(0, 6)
        self.nextFigure = random.randint(0, 6)
        self.cells = self.newPosition(self.currentFigure)

    def createFigure(self, figure):
        cells = []
        for x, y in figures[figure]:
            cells.append((width // 2 + (x - 1), y + 1))
        return cells

    # Collision, needed for the movements
    def collision(self, cells):
        for x, y in cells:
            if x < 0 or x > width - 1 or y > height - 1:
                return True
            if y >= 0 and self.board[y][x] != 0:
                return True
        return False

    # Moving the pieces
    #def left(self):

    #def right(self):



    def toDict(self):

        return {
            "plateau": self.plateau,
            "score": self.score,
            "niveau": self.niveau,
            "partie_terminee": self.partie_terminee,
        }