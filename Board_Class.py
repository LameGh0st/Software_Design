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

    def legal_placement(self, ship, cor):
        direct_dict = {"North": (0,-1),
                       "South": (0,1),
                       "East": (1,0),
                       "West": (-1,0)}
        dir = direct_dict[ship.direction]
        x,y = cor
        y += -1
        x += -1
        if x < 1 or y < 1:
            return False
        if x >= self.width or y >= self.length:
            return False
        a,b = dir
        if self.board[y][x] == 1:
            return False
        for i in range(ship.length-1):
            y += b
            x += a
            if x < 0 or y < 0:
                return False
            if x >= self.width or y >= self.length:
                return False
            if self.board[y][x] == 1:
                return False
        return True


    def place_ship(self, ship, cor):
        direct_dict = {"North": (0,-1),
                       "South": (0,1),
                       "East": (1,0),
                       "West": (-1,0)}
        dir = direct_dict[ship.direction]
        x,y = cor
        y += -1
        x += -1
        a,b = dir
        self.board[y][x] = 1
        ship.ship_cords.append((x,y))
        for i in range(ship.length-1):
            y += b
            x += a
            self.board[y][x]=1
            ship.ship_cords.append((x,y))
        self.ships_on_board.append(ship)
        


if __name__ == '__main__':
    pass
    
        

