from matplotlib.style import available
from Board_Class import *
from Ship_Class import *
from graphics import *
import Helpers as help
import Constants as cons
from AbstractPlayer import AbstractPlayer

class HumanPlayer(AbstractPlayer):

    def __init__(self):
        self.hidden_board = Board(10,10)
        self.guess_board = Board(10,10)
#-----------------------------------------------------------------------------
    def placement(self, win, known_rectangles):
        carrier = Ship(5, "North", "carrier")
        battleship = Ship(4, "North", "battleship")
        submarine = Ship(3, "North", "submarine")
        destroyer = Ship(3, "North", "destroyer")
        cruiser = Ship(2, "North", "cruiser")
        ship_list = [carrier, battleship, submarine, destroyer, cruiser]
        direction_list = {(0,-1): "North",
                        (0,1): "South",
                        (1,0): "East",
                        (-1,0): "West"}
        for ship in ship_list:
            help.show_board(self.hidden_board.board)
            # Get Cord
            point = win.getMouse()
            while (point.getX() <= cons.offset or point.getX() >= cons.width - cons.offset
            or point.getY() <= cons.offset or point.getY() >= cons.length - cons.offset):
                point = win.getMouse()
            x = point.getX() - cons.offset
            y = point.getY() - cons.offset
            x = int(x  // cons.delta_width)
            y = int(y  // cons.delta_length)
            cord1 = (x,y)
            help.available_placement(cord1, self.hidden_board, known_rectangles, ship)

            #Get direction
            point = win.getMouse()
            while (point.getX() <= cons.offset or point.getX() >= cons.width - cons.offset
            or point.getY() <= cons.offset or point.getY() >= cons.length - cons.offset):
                point = win.getMouse()
            while ((point.getX() - cons.offset) // cons.delta_width - x, 
            (point.getY() - cons.offset)//cons.delta_length - y) not in direction_list:
                point = win.getMouse()
            x = point.getX() - cons.offset
            y = point.getY() - cons.offset
            x = int(x  // cons.delta_width)
            y = int(y  // cons.delta_length)
            cord2 = (x,y)
            direction = (cord2[0] - cord1[0], cord2[1] - cord1[1])
            direction = direction_list[direction]

            ship.direction = direction
            while self.hidden_board.legal_placement(ship, cord1) == False:
                help.show_ships(self.hidden_board, known_rectangles)

                print("Cannot place a ship there")
                point = win.getMouse()
                while (point.getX() <= cons.offset or point.getX() >= cons.width - cons.offset
                or point.getY() <= cons.offset or point.getY() >= cons.length - cons.offset):
                    point = win.getMouse()
                x = point.getX() - cons.offset
                y = point.getY() - cons.offset
                x = int(x  // cons.delta_width)
                y = int(y  // cons.delta_length)
                cord1 = (x,y)
                help.available_placement(cord1, self.hidden_board, known_rectangles, ship)

                #Get direction
                point = win.getMouse()
                while (point.getX() <= cons.offset or point.getX() >= cons.width - cons.offset
                or point.getY() <= cons.offset or point.getY() >= cons.length - cons.offset):
                    point = win.getMouse()
                x = point.getX() - cons.offset
                y = point.getY() - cons.offset
                x = int(x  // cons.delta_width)
                y = int(y  // cons.delta_length)
                cord2 = (x,y)
                direction = (cord2[0] - cord1[0], cord2[1] - cord1[1])
                direction = direction_list[direction]


            ship.direction = direction
            self.hidden_board.place_ship(ship, cord1)
            help.show_ships(self.hidden_board, known_rectangles)

        help.show_board(self.hidden_board.board)
#-----------------------------------------------------------------------------
    def move(self, win_guess_board):
        print("Your turn\n")
        help.show_board(cons.player_guess_board.board)
        print("Click a spot to fire at!\n")
        point = win_guess_board.getMouse()
        while (point.getX() <= cons.offset or point.getX() >= cons.width - cons.offset
            or point.getY() <= cons.offset or point.getY() >= cons.length - cons.offset):
            point = win_guess_board.getMouse()
        x = point.getX() - cons.offset
        y = point.getY() - cons.offset
        x = int(x  // cons.delta_width)
        y = int(y  // cons.delta_length)
        cord = (x,y)
        return cord
#-----------------------------------------------------------------------------
    def process(self, cord, result, ship_cords, sunk_ship_length):
        x,y = cord
        if result == 'Miss':
            self.guess_board.board[y][x] = 'M'
        else:
            self.guess_board.board[y][x] = 'X'
#-----------------------------------------------------------------------------
    def lookup(self, cord):
        return super().lookup(cord)