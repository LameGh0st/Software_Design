from Board_Class import *
from Ship_Class import *


#-----------------------------------------------------------------------------
def get_coords(cord):
    letter = cord[0]
    num = cord[1:]
    return (ord(letter)-65,int(num)-1)
#-----------------------------------------------------------------------------
def get_board_values(board):
    sum = 0
    for i in range(len(board)):
        for j in board[i]:
            sum += j
    return sum
#-----------------------------------------------------------------------------
def show_board(board):
    for i in board:
        print(i)
        print('')
#-----------------------------------------------------------------------------
def Fire(Cor, board):
    a,b = Cor
    if board.board[a][b] == 1:
        return True
    else:
        return False
#-----------------------------------------------------------------------------
def play_game():
    public_board = Board(10,10)
    hidden_board = Board(10,10)
    battleship = Ship(5, "North")
    submarine = Ship(3, "West")
    hidden_board.place_ship(battleship, (1,1), 5, "North")
    hidden_board.place_ship(submarine, (5,5), 3, "West")
    #show_board(hidden_board.board)
    #hidden_board.place_ship((2,1),4)
    #hidden_board.place_ship((5,5),3)
    cords_shot_at = []
    values_on_board = get_board_values(hidden_board.board)
    show_board(public_board.board)
    while 0 < values_on_board:
        val = input("Choose a coordinate to fire at!\n")
        cord = get_coords(val)
        if cord not in cords_shot_at:
            cords_shot_at.append(cord)
            x,y = cord
            if Fire(cord, hidden_board):
                hidden_board.board[x][y] = "X"
                public_board.board[x][y] = 'X'
                for ship in hidden_board.ships_on_board:
                    if (y,x) in ship.ship_cords:
                        ship.hp -= 1
                        if ship.hp == 0:
                            print("Hit!")
                            print("You sunk a ship!")
                        else:
                            print("Hit!")
                show_board(public_board.board)
                values_on_board += -1
            else:
                hidden_board.board[x][y] = "O"
                public_board.board[x][y] = 'O'
                print("Miss!")
                show_board(public_board.board)
        else:
            print("You already fired at that location, choose a different coordinate")
    print("Congrats you win!\nYou sunk all of the enemy ships")
#-----------------------------------------------------------------------------


if __name__ == '__main__':
    play_game()