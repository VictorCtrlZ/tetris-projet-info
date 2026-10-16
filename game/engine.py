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
FALL_SPEED = 1000
FAST_FALL_SPEED = 50

#Jeu solo
class Tetris:

    # Le __init__ est la première méthode éxécutée lors de la création d'une partie
    # On y crée toutes les choses nécessaires pour la partie
    def __init__(self):
        self.board = []
        for y in range(height):
            line = []
            for x in range(width):
                line.append((0))
            self.board.append(line)

        self.score = 0
        self.gameOver = False

        self.fallSpeed = FALL_SPEED
        self.time = 0

        self.currentFigure = random.randint(0, 6)
        self.nextFigure = random.randint(0, 6)
        self.cells = self.createFigure(self.currentFigure)

    def createFigure(self, figure):
        cells = []
        for x, y in figures[figure]:
            cells.append((width // 2 + (x - 1), y + 1))
        return cells

    # Collision, needed for the movements
    def collision(self, cells):
        for x, y in cells:
            if x < 0 or x >= width or y < 0 or y >= height:
                return True
            if self.board[y][x] != 0:
                return True
        return False

    # Moving the pieces
    def left(self):
        if self.gameOver:
            return
        newCells = []
        for x, y in self.cells:
            newCells.append( ( x - 1, y ) )
        if self.collision(newCells) == False:
            self.cells = newCells

    def right(self):
        if self.gameOver:
            return
        newCells = []
        for x, y in self.cells:
            newCells.append( ( x + 1, y ) )
        if self.collision(newCells) == False:
            self.cells = newCells

    def rotate(self):
        centerX, centerY = self.cells[0]
        newCells = []
        for x, y in self.cells:
            offsetX = x - centerX
            offsetY = y - centerY

            newX = centerX - offsetY
            newY = centerY + offsetX

            newCells.append((newX,newY))
        if self.collision(newCells) == False:
            self.cells = newCells

    def toDict(self):
        return {
            "width": width,
            "height": height,
            "board": self.board,
            "score": self.score,
            "gameOver": self.gameOver,
            "fallSpeed": self.fallSpeed,
            "time": self.time,
            "currentFigure": self.currentFigure,
            "nextFigure": self.nextFigure,
            "cells": self.cells
        }