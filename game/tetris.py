SHAPES = {
    "I":[
        [1,1,1,1]
    ],
    "O": [
        [1,1],
        [1,1]
    ],
    "T": [
        [1,1,1],
        [0,1,0]
    ],
    "L":[
        [1,1,1],
        [1,0,0]
    ],
    "J":[
        [1,1,1],
        [0,0,1]
    ],
    "Z": [
        [1,1,0],
        [0,1,1]
    ],
    "S": [
        [0,1,1],
        [1,1,0]
    ]
}


class Tetris:
    def __init__(self):
        self.width = 10
        self.height = 20


        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

        self.x=0
        self.y=0

        self.shape = None #pièce qui est actuellement en train de tomber

        self.score = 0

