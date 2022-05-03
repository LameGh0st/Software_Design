from Board_Class import *
import Helpers as help


class AbstractPlayer:
    def __init__(self):
        self.hidden_board = Board(10,10)
        self.guess_board = Board(10,10)
#-----------------------------------------------------------------------
    def get_ship_cords(self, cord):
        for ship in self.hidden_board.ships_on_board:
            if cord in ship.ship_cords:
                return ship.ship_cords
#-----------------------------------------------------------------------
    def placement(self):
        raise NotImplementedError()
#-----------------------------------------------------------------------
    def move(self):
        raise NotImplementedError()
#-----------------------------------------------------------------------
    def process(self, cord, result, ship_cords, sunk_ship_length):
        raise NotImplementedError()
#-----------------------------------------------------------------------
    def lookup(self, cord):
        x,y = cord
        if help.fire(cord,self.hidden_board):
            self.hidden_board.board[y][x] = "X"
            self.hidden_board.hp -= 1
            if self.hidden_board.hp == 0:
                return ["Game Over", [], None]
            for ship in self.hidden_board.ships_on_board:
                if cord in ship.ship_cords:
                    ship.hp -= 1
                    if ship.hp == 0:
                        ship_cords = self.get_ship_cords(cord)
                        return ["Sunk", ship_cords, ship.size]
            return ["Hit", [], None]
        else:
            self.hidden_board.board[y][x] = "M"
            return ["Miss", [], None]
#-----------------------------------------------------------------------
    def reset(self):
        self.hidden_board.reset()
        self.guess_board.reset()

