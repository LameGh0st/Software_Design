import random as rand

class Board:
    def __init__(self,length, width):
        self.width = width
        self.length = length
        self.board = []
        for i in range(self.length):
            row = []
            for j in range(self.width):
                row.append('0')
            self.board.append(row)
        self.ships_on_board = []
        self.possible_cords = []
        for i in range(self.length):
            for j in range(self.width):
                self.possible_cords.append((j, i))
        self.cords_shot_at = []
        

    def legal_placement(self, ship, cor):
        direct_dict = {"North": (0,-1),
                       "South": (0,1),
                       "East": (1,0),
                       "West": (-1,0)}
        dir = direct_dict[ship.direction]
        x,y = cor
        if x < 0 or y < 0:
            return False
        if x >= self.width or y >= self.length:
            return False
        a,b = dir
        if self.board[y][x] == '1':
            return False
        for i in range(ship.size-1):
            y += b
            x += a
            if x < 0 or y < 0:
                return False
            if x >= self.width or y >= self.length:
                return False
            if self.board[y][x] == '1':
                return False
        return True


    def place_ship(self, ship, cor):
        direct_dict = {"North": (0,-1),
                       "South": (0,1),
                       "East": (1,0),
                       "West": (-1,0)}
        dir = direct_dict[ship.direction]
        x,y = cor
        a,b = dir
        self.board[y][x] = '1'
        ship.ship_cords.append((x,y))
        for i in range(ship.size-1):
            y += b
            x += a
            print((x,y), (a,b), ship.direction)
            self.board[y][x]= '1'
            ship.ship_cords.append((x,y))
        self.ships_on_board.append(ship)
        


if __name__ == '__main__':
    public_board = Board(10,10)
    print(public_board.possible_cords)
    
        

