from Board_Class import *
import Helpers as help


class AbstractPlayer:
    def __init__(self):
        self.hidden_board = Board(10,10)
        self.guess_board = Board(10,10)

    def placement(self):
        raise NotImplementedError()

    def move(self):
        raise NotImplementedError()

    def process(self, cord, result):
        raise NotImplementedError()

    def lookup(self, cord):
        x,y = cord
        if help.fire(cord,self.hidden_board.board[y][x]):
            self.hidden_board.board[y][x] = "X"
            for ship in self.hidden_board.ships_on_board:
                if (x,y) in ship.ship_cords:
                    ship.hp -= 1
                    if ship.hp == 0:
                        return "Sunk"
            return "Hit"
        else:
            self.hidden_board[y][x] = "M"
            return "Miss"

