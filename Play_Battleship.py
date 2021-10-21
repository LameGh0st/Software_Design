from Board_Class import *
from Ship_Class import *
import random


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
    direction_list = ["North", "South", "East", "West"]
    direction = random.choice(direction_list)
    x = random.randint(0, hidden_board.width-1)
    y = random.randint(0, hidden_board.length-1)
    while hidden_board.legal_placement(battleship, (x,y), battleship.size, direction) == False:
        x = random.randint(0, hidden_board.width-1)
        y = random.randint(0, hidden_board.length-1)
        direction = random.choice(direction_list)
    hidden_board.place_ship(battleship, (x,y), battleship.size, direction)
    x = random.randint(0, hidden_board.width-1)
    y = random.randint(0, hidden_board.length-1)
    direction = random.choice(direction_list)
    while hidden_board.legal_placement(submarine, (x,y), submarine.size, direction) == False:
        x = random.randint(0, hidden_board.width-1)
        y = random.randint(0, hidden_board.length-1)
        direction = random.choice(direction_list)
    hidden_board.place_ship(submarine, (x,y), submarine.size, direction)
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