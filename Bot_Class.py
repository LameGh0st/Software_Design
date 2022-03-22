from logging import NullHandler
import random
from Ship_Class import *
import Helpers as help

class Bot:
    def __init__(self):
        self.destroy_mode = False
        self.first_known_hit = None
        self.last_known_hit = None
        self.direction = None
        self.last_shot = None
        self.known_hits = []

        
#------------------------------------------------------------------------------
    def bot_placement(self, Board):
        carrier = Ship(5, "North", "carrier")
        battleship = Ship(4, "North", "battleship")
        submarine = Ship(3, "North", "submarine")
        destroyer = Ship(3, "North", "destroyer")
        cruiser = Ship(2, "North", "curiser")
        ship_list = [carrier, battleship, submarine, destroyer, cruiser]
        for ship in ship_list:
            direction, x, y = help.direction_list(Board)
            ship.direction = direction
            while Board.legal_placement(ship, (x,y)) == False:
                direction, x, y = help.direction_list(Board)
                ship.direction = direction
            ship.direction = direction
            Board.place_ship(ship, (x,y))
#------------------------------------------------------------------------------
    def search(self, bot_guess_board, player_hidden_board, board_of_rectangles, cords):
        print('search')
        cord = cords[0] 
        x,y = cord
        cords.remove(cord)
        if help.fire(cord, player_hidden_board):
            self.last_shot = cord
            self.destroy_mode = True
            self.last_known_hit = cord
            self.known_hits.append(cord)
            self.first_known_hit = cord
            bot_guess_board.board[y][x] = 'X'
            player_hidden_board.board[y][x] = 'X'
            board_of_rectangles[y][x].setFill('red')
            bot_guess_board.cords_shot_at.append(cord)
            for ship in player_hidden_board.ships_on_board:
                if (x,y) in ship.ship_cords:
                    ship.hp -= 1
                    if ship.hp == 0:
                        print("Hit!")
                        print("The AI sunk a ship!")
                        for i in ship.ship_cords:
                            x,y = i
                            board_of_rectangles[y][x].setFill('black')
                    else:
                        print("Hit!")
            player_hidden_board.hp -= 1
            #help.show_board(bot_guess_board.board)
        else:
            self.last_shot = cord
            bot_guess_board.board[y][x] = 'M'
            player_hidden_board.board[y][x] = 'M'
            board_of_rectangles[y][x].setFill('white')
            bot_guess_board.cords_shot_at.append(cord)
            print('Miss')
            #help.show_board(bot_guess_board.board)
#------------------------------------------------------------------------------
    def destroy(self, bot_guess_board, player_hidden_board, board_of_rectangles, cords):
        print('destroy')
        dir_list = [(0,-1),(0,1),(1,0),(-1,0)]
        random.shuffle(dir_list)
        if self.direction == None:
            self.direction = dir_list
        if len(self.direction) == 0 and self.first_known_hit == None:
            self.destroy_mode = False 
            self.last_known_hit = None
            self.first_known_hit = None
            self.direction = None
            self.search(bot_guess_board, player_hidden_board, board_of_rectangles, cords)
            return None
        for ship in player_hidden_board.ships_on_board:
                if self.last_known_hit in ship.ship_cords:
                    if ship.hp == 0:
                        self.first_known_hit = None
                        self.direction = None
                        for i in ship.ship_cords:
                            if i in self.known_hits:
                                self.known_hits.remove(i)
                        if len(self.known_hits) == 0:
                            self.destroy_mode = False 
                            self.last_known_hit = None
                            self.first_known_hit = None
                            self.direction = None
                            self.search(bot_guess_board, player_hidden_board, board_of_rectangles, cords)
                            return None
                        if len(self.known_hits) != 0:
                            self.last_known_hit = self.known_hits.pop()
                            self.first_known_hit = self.last_known_hit
                            self.direction = [(0,-1),(0,1),(1,0),(-1,0)]
                            random.shuffle(self.direction)
                            self.direction

        dx,dy = self.direction[0]
        x,y = self.last_known_hit
        new_cord = (x+dx,y+dy)
        while not help.legal_shot(bot_guess_board, new_cord):
            self.direction = self.direction[1:]
            if len(self.direction) == 0:
                self.destroy_mode = False 
                self.last_known_hit = None
                self.first_known_hit = None
                self.direction = None
                self.search(bot_guess_board, player_hidden_board, board_of_rectangles, cords)
                return None
            dx,dy = self.direction[0]
            x,y = self.first_known_hit
            new_cord = (x+dx, y+dy)
        
        cords.remove(new_cord)
        x,y = new_cord
        if help.fire(new_cord, player_hidden_board):
            self.last_known_hit = new_cord
            self.last_shot = new_cord
            self.known_hits.append(new_cord)
            bot_guess_board.board[y][x] = 'X'
            player_hidden_board.board[y][x] = 'X'
            board_of_rectangles[y][x].setFill('red')
            bot_guess_board.cords_shot_at.append(new_cord)
            for ship in player_hidden_board.ships_on_board:
                if (x,y) in ship.ship_cords:
                    ship.hp -= 1
                    if ship.hp == 0:
                        print("Hit!")
                        print("The AI sunk a ship!")
                        for i in ship.ship_cords:
                            x,y = i
                            board_of_rectangles[y][x].setFill('black')
                    else:
                        print("Hit!")
            player_hidden_board.hp -= 1
            #help.show_board(bot_guess_board.board)
        else:
            self.direction = self.direction[1:]
            self.last_known_hit = self.first_known_hit
            self.last_shot = new_cord
            bot_guess_board.board[y][x] = 'M'
            player_hidden_board.board[y][x] = 'M'
            board_of_rectangles[y][x].setFill('white')
            bot_guess_board.cords_shot_at.append(new_cord)
            print('Miss')
            #help.show_board(bot_guess_board.board)
        