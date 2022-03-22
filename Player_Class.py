from matplotlib.style import available
from Board_Class import *
from Ship_Class import *
from graphics import *
import Helpers as help
import Constants as cons

class Player:

    def __init__(self):
        pass
#-----------------------------------------------------------------------------
    def player_placement(self, board, win, known_rectangles):
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
            help.show_board(board.board)
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
            help.available_placement(cord1, board, known_rectangles, ship)

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
            while board.legal_placement(ship, cord1) == False:
                help.show_ships(board, known_rectangles)

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
                help.available_placement(cord1, board, known_rectangles, ship)

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
            board.place_ship(ship, cord1)
            help.show_ships(board, known_rectangles)

        help.show_board(board.board)
#-----------------------------------------------------------------------------
    def player_turn(self, player_guess_board, bot_hidden_board, board_of_rectangles, cord):
        player_guess_board.cords_shot_at.append(cord)
        x,y = cord
        if help.fire(cord, bot_hidden_board):
            bot_hidden_board.board[y][x] = "X"
            player_guess_board.board[y][x] = 'X'
            board_of_rectangles[y][x].setFill('red')
            for ship in bot_hidden_board.ships_on_board:
                if (x,y) in ship.ship_cords:
                    ship.hp -= 1
                    if ship.hp == 0:
                        print("Hit!")
                        print("You sunk a {name}".format(name = ship.name))
                        for i in ship.ship_cords:
                            x,y = i
                            board_of_rectangles[y][x].setFill('black')
                    else:
                        print("Hit!")
            bot_hidden_board.hp -= 1
            help.show_board(player_guess_board.board)
        else:
            bot_hidden_board.board[y][x] = "M"
            player_guess_board.board[y][x] = 'M'
            board_of_rectangles[y][x].setFill('white')
            print("Miss!")
            help.show_board(player_guess_board.board)