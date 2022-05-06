from logging import NullHandler
import random
from Ship_Class import *
from Board_Class import *
import Helpers as help
import Constants as cons
from AbstractPlayer import AbstractPlayer

class Smarter_Bot(AbstractPlayer):
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
        self.ships_left = [5,4,3,3,2]

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
    def process(self, cord, result, ship_cords, sunk_ship_length):
        x,y = cord
        if not self.destroy_mode and result == "Miss":
            self.guess_board.board[y][x] = "M"
            self.guess_board.cords_shot_at.append(cord)
            self.last_shot = cord
        elif not self.destroy_mode and result == "Hit":
            self.guess_board.board[y][x] = "X"
            self.guess_board.cords_shot_at.append(cord)
            self.known_hits.append(cord)
            self.last_shot = cord
            self.destroy_mode = True
            self.last_known_hit = cord
            self.first_known_hit = cord
        elif self.destroy and result == "Hit":
            self.guess_board.board[y][x] = "X"
            self.guess_board.cords_shot_at.append(cord)
            self.known_hits.append(cord)
            self.last_shot = cord
            self.last_known_hit = cord
        elif self.destroy_mode and result == "Miss":
            self.guess_board.board[y][x] = "M"
            self.guess_board.cords_shot_at.append(cord)
            self.last_shot = cord
            self.last_known_hit = self.first_known_hit
        elif self.destroy_mode and result == "Sunk":
            self.guess_board.board[y][x] = "X"
            self.ships_left.remove(sunk_ship_length)
            self.guess_board.cords_shot_at.append(cord)
            self.known_hits.append(cord)
            self.first_known_hit = None
            self.direction = None
            for i in ship_cords:
                if i in self.known_hits:
                    self.known_hits.remove(i)
            if len(self.known_hits) == 0:
                self.destroy_mode = False 
                self.last_known_hit = None
                self.first_known_hit = None
                self.direction = None
                self.search()
            if len(self.known_hits) != 0:
                self.last_known_hit = self.known_hits.pop()
                self.first_known_hit = self.last_known_hit
                self.direction = [(0,-1),(0,1),(1,0),(-1,0)]
                random.shuffle(self.direction)
                self.direction

        
        
                
#------------------------------------------------------------------------------
    def lookup(self, cord):
        return super().lookup(cord)
#------------------------------------------------------------------------------
    def check_vertical(self, cord, size):
        count = 1
        x,y = cord
        dx,dy = (0,-1)
        new_cord = (x+dx, y+dy)
        while help.legal_shot(self.guess_board, new_cord):
            count += 1
            x,y = new_cord
            new_cord = (x+dx, y+dy)
        if count >= size:
            return True
        x,y = cord
        dx,dy = (0,1)
        new_cord = (x+dx, y+dy)
        while help.legal_shot(self.guess_board, new_cord):
            count += 1
            x,y = new_cord
            new_cord = (x+dx, y+dy)
        if count >= size:
            return True
        return False
#------------------------------------------------------------------------------
    def check_horizontal(self, cord, size):
        count = 1
        x,y = cord
        dx,dy = (-1,0)
        new_cord = (x+dx, y+dy)
        while help.legal_shot(self.guess_board, new_cord):
            count += 1
            x,y = new_cord
            new_cord = (x+dx, y+dy)
        if count >= size:
            return True
        x,y = cord
        dx,dy = (1,0)
        new_cord = (x+dx, y+dy)
        while help.legal_shot(self.guess_board, new_cord):
            count += 1
            x,y = new_cord
            new_cord = (x+dx, y+dy)
        if count >= size:
            return True
        return False
            

#------------------------------------------------------------------------------
    def search(self):
        cord = self.possible_cords[0] 
        while not self.check_vertical(cord, self.ships_left[0]) and not self.check_horizontal(cord, self.ships_left[0]):
            self.possible_cords.remove(cord)
            self.possible_cords.append(cord)
            cord = self.possible_cords[0]
        self.possible_cords.remove(cord)
        return cord

#------------------------------------------------------------------------------
    def destroy(self):
        dir_list = [(0,-1),(0,1),(1,0),(-1,0)]
        random.shuffle(dir_list)
        if self.direction == None:
            self.direction = dir_list
        if len(self.direction) == 0 and self.first_known_hit == None:
            self.destroy_mode = False 
            self.last_known_hit = None
            self.first_known_hit = None
            self.direction = None
            return self.search()
        dx,dy = self.direction[0]
        x,y = self.last_known_hit
        new_cord = (x+dx,y+dy)
        while not help.legal_shot(self.guess_board, new_cord):
            if self.last_known_hit != self.first_known_hit:
                self.direction.remove((dx,dy))
                if (-dx,-dy) in self.direction:
                    self.direction.remove((-dx,-dy))
                    self.direction = [(-dx,-dy)] + self.direction
            else:
                self.direction = self.direction[1:]

            
            if len(self.direction) == 0:
                self.destroy_mode = False 
                self.last_known_hit = None
                self.first_known_hit = None
                self.direction = None
                return self.search()

            dx,dy = self.direction[0]
            x,y = self.first_known_hit
            new_cord = (x+dx, y+dy)
        
        if new_cord in self.possible_cords:
            self.possible_cords.remove(new_cord)
        return new_cord
#------------------------------------------------------------------------------
    def reset(self):
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
        self.ships_left = [5,4,3,3,2]       