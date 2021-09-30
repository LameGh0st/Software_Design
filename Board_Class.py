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


    def place_ship(self, cor, length):
        a,b = cor
        for i in range(length):
            self.board[b-1+i][a-1]=1
        


if __name__ == '__main__':
    pass
    
        

