from Board_Class import *



class AbstractPlayer:
    def __init__(self):
        self.hidden_board = Board(10,10)
        self.guess_board = Board(10,10)

    def placement(self):
        raise NotImplementedError()

    def move(self):
        raise NotImplementedError()

    def process(self):
        raise NotImplementedError()

    def lookup(self, cord):
        x,y = cord
        return self.hidden_board.board[y][x]