from Board_Class import *




def get_coords(cord):
    letter = cord[0]
    num = cord[1:]
    return (ord(letter)-65,int(num)-1)


def get_board_values(board):
    vals = []
    for i in range(len(board)):
        for j in board[i]:
            vals.append(j)
    return vals

def show_board(board):
    for i in board:
        print(i)
        print('')


def Fire(Cor, board):
    a,b = Cor
    if board.board[a][b] == 1:
        return True
    else:
        return False



if __name__ == '__main__':
    public_board = Board(10,10)
    hidden_board = Board(10,10)
    hidden_board.place_ship((1,1), 5)
    cords_shot_at = []
    values_on_board = get_board_values(hidden_board.board)
    show_board(public_board.board)
    while 1 in values_on_board:
        val = input("Choose a coordinate to fire at!\n")
        cord = get_coords(val)
        if cord not in cords_shot_at:
            cords_shot_at.append(cord)
            a,b = cord
            if Fire(cord, hidden_board):
                hidden_board.board[a][b] = "X"
                public_board.board[a][b] = 'X'
                print("Hit!")
                show_board(public_board.board)
                values_on_board = get_board_values(hidden_board.board)
            else:
                hidden_board.board[a][b] = "O"
                public_board.board[a][b] = 'O'
                print("Miss!")
                show_board(public_board.board)
                values_on_board = get_board_values(hidden_board.board)
        else:
            print("You already fired at that location, choose a different coordinate")
    print("Congrats you win!\nYou sunk all of the enemy ships")