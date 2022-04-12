from logging import NullHandler
import random
from Ship_Class import *
from Board_Class import *
import Helpers as help
import Constants as cons
from AbstractPlayer import AbstractPlayer

class Bot(AbstractPlayer):
    def __init__(self):
        self.hidden_board = Board(10,10)
        self.guess_board = Board(10,10)
        self.destroy_mode = False
        self.first_known_hit = None
        self.last_known_hit = None
        self.direction = None
        self.last_shot = None
        self.known_hits = []
        self.possible_cords = []
        for i in range(cons.bot_guess_board.length):
                for j in range(cons.bot_guess_board.width):
                    self.possible_cords.append((j, i))
        random.shuffle(self.possible_cords)

#------------------------------------------------------------------------------
    def placement(self):
        carrier = Ship(5, "North", "carrier")
        battleship = Ship(4, "North", "battleship")
        submarine = Ship(3, "North", "submarine")
        destroyer = Ship(3, "North", "destroyer")
        cruiser = Ship(2, "North", "curiser")
        ship_list = [carrier, battleship, submarine, destroyer, cruiser]
        for ship in ship_list:
            direction, x, y = help.direction_list(self.hidden_board)
            ship.direction = direction
            while self.hidden_board.legal_placement(ship, (x,y)) == False:
                direction, x, y = help.direction_list(self.hidden_board)
                ship.direction = direction
            ship.direction = direction
            self.hidden_board.place_ship(ship, (x,y))
#------------------------------------------------------------------------------
    def move(self, win_board):
        if self.destroy_mode:
            return self.destroy()
        else:
            return self.search()
#------------------------------------------------------------------------------
    def search(self):
        print('search')
        cord = self.possible_cords[0] 
        x,y = cord
        self.possible_cords.remove(cord)
        return cord

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
        