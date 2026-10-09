import random

width = 10
height = 20

figures = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],   # 0 : la barre (I)
    [(0, 2), (0, 1), (1, 1), (1, 0)],  # 1 : S
    [(0, 0), (0, 1), (1, 1), (1, 2)],    # 2 : Z
    [(0, 0), (0, 1), (1, 0), (1, 1)],     # 3 : le carré (O)
    [(0, 1), (0, 0), (1, 0), (2, 0)],     # 4 : L
    [(0, 0), (1, 0), (2, 0), (2, 1)],     # 5 : J
    [(0, 0), (1, 0), (1, 1), (2, 0)],     # 6 : T
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
                line.append([])
            self.board.append(line)

        self.score = 0
        self.gameOver = False

        self.fallSpeed = fallSpeed
        self.fastFallSpeed = fastFallSpeed
        self.time = 0

        self.currentFigure = random.randint(0, 6)
        self.nextFigure = random.randint(0, 6)
        self.cells = self.newPosition(self.currentFigure)

    def newPosition(self, figure):
        cells = []
        for x, y in figures[figure]:
            cells.append((width // 2 + (x - 1), y + 1))
        return cells

    def toDict(self):

        return {
            "width": width,
            "height": height,
            "board": self.board,
            "score": self.score,
            "gameOver": self.gameOver,
            "fallSpeed": self.fallSpeed,
            "fastFallSpeed": self.fastFallSpeed,
            "time": self.time,
            "currentFigure": self.currentFigure,
            "nextFigure": self.nextFigure,
            "cells": self.cells
        }