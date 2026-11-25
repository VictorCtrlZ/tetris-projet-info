import random

width = 10
height = 20

figures = [
    [(1, 0), (0, 0), (2, 0), (3, 0)],   # 0 : I, pivot (1, 0)
    [(0, 1), (0, 2), (1, 1), (1, 0)],   # 1 : S, pivot (0, 1)
    [(0, 1), (0, 0), (1, 1), (1, 2)],   # 2 : Z, pivot (0, 1)
    [(0, 0), (0, 1), (1, 0), (1, 1)],   # 3 : square, does not rotate
    [(1, 0), (0, 1), (0, 0), (2, 0)],   # 4 : L, pivot (1, 0)
    [(1, 0), (0, 0), (2, 0), (2, 1)],   # 5 : J, pivot (1, 0)
    [(1, 0), (0, 0), (1, 1), (2, 0)],   # 6 : T, pivot (1, 0)
]

points = {0 : 0, 1 : 100, 2 : 300, 3 : 700, 4 : 1500}

# Speed in ms
FALL_SPEED = 1000
FAST_FALL_SPEED = 250

#Solo game
class Tetris:

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

        self.fastFall = False

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

    def rotation(self):

        if not self.gameOver and not self.currentFigure == 3: # 3 is the square -> exception

            centerX, centerY = self.cells[0] # Pivot
            newCells = []

            for x, y in self.cells:
                offsetX = x - centerX # The distance to the pivot for each part of the figure
                offsetY = y - centerY

                # New positions coordinates :
                newX = centerX - offsetY
                newY = centerY + offsetX

                newCells.append((newX, newY))

            if self.collision(newCells) == False:
                self.cells = newCells

        else :
            return

    def clearLine(self):
        keptLines = []  # Defining the lines to keep : if there's a 0, the case is empty, so we keep it
        for line in self.board :
            if 0 in line :
                keptLines.append(line)
            # Or, the line is full, we remove it

        removed = height - len(keptLines)

        newLines = [] # Recreating the lines that have been removed
        for i in range(removed):
            line = []
            for x in range(width):
                line.append(0)
            newLines.append(line)

        # We recreate the board with the new lines
        self.board = newLines + keptLines

        return removed # Will be useful for the score

    def nextPiece(self):
        # We save the current figure and define the next one already
        self.currentFigure = self.nextFigure
        self.nextFigure = random.randint(0, 6)
        self.cells = self.createFigure(self.currentFigure)

        # Check if there are collisions with the new coordinates, if yes, game over
        if self.collision(self.cells) :
            self.gameOver = True

    def lockPiece(self):
        for x, y in self.cells:
            if y >= 0 :
                self.board[y][x] = self.currentFigure + 1 # 0 means empty, so we use +1

        removed = self.clearLine() # clearLine returns how many lines have been removed

        self.score += points[removed]

        if not self.gameOver :
            self.nextPiece()

    def fall(self):
        if self.gameOver:
            return False

        newCells = []
        for x, y in self.cells:
            newCells.append((x, y + 1))

        if self.collision(newCells) == False:
            self.cells = newCells
            return True # The figure fell, no collision
        return False # collision

    def setFastFall(self, on) :
        self.fastFall = on

    def tick(self, ms):
        if self.gameOver :
            return

        if self.fastFall :
            speed = FAST_FALL_SPEED
        else :
            speed = self.fallSpeed

        self.time += ms

        if self.time < speed :
            return

        self.time = 0
        if not self.fall(): # If no collision
            self.lockPiece() # The bottom is reached, locking the piece

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