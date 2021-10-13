class Board:
    def __init__(self,length, width):
        self.width = width
        self.length = length
        self.board = []
        for i in range(self.length):
            row = []
            for j in range(self.width):
                row.append(0)
            self.board.append(row)
        self.ships_on_board = []


    def place_ship(self, Ship, cor, length, direction):
        direct_dict = {"North": (0,-1),
                       "South": (0,1),
                       "East": (1,0),
                       "West": (-1,0)}
        dir = direct_dict[direction]
        x,y = cor
        y += -1
        x += -1
        a,b = dir
        self.board[y][x] = 1
        Ship.ship_cords.append((x,y))
        for i in range(length-1):
            y += b
            x += a
            self.board[y][x]=1
            Ship.ship_cords.append((x,y))
        self.ships_on_board.append(Ship)
        


if __name__ == '__main__':
    pass
    
        

