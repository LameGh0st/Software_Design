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
            sum += int(j)
    return sum
#-----------------------------------------------------------------------------
def show_board(board):
    letters = []
    nums = []
    for i in range(len(board)):
        letters.append(chr(65+i))
    for i in range(len(board)):
        print(letters[i], board[i])
        print('')
    for i in range(len(board[0])):
        nums.append(str(i+1))
    print(' ', nums)
#-----------------------------------------------------------------------------
def Fire(Cor, board):
    a,b = Cor
    if board.board[a][b] == 1:
        return True
    else:
        return False
#-----------------------------------------------------------------------------
def direction_list(board):
    direction_list = ["North", "South", "East", "West"]
    direction = random.choice(direction_list)
    x = random.randint(0, board.width-1)
    y = random.randint(0, board.length-1)
    return [direction, x, y]
#-----------------------------------------------------------------------------
def bot_placement(board):
    carrier = Ship(5, "North")
    battleship = Ship(4, "North")
    submarine = Ship(3, "North")
    destroyer = Ship(3, "North")
    cruiser = Ship(2, "North")
    ship_list = [carrier, battleship, submarine, destroyer, cruiser]
    for ship in ship_list:
        dir_list = direction_list(board)
        direction, x, y = dir_list[0], dir_list[1], dir_list[2]
        while board.legal_placement(ship, (x,y)) == False:
            dir_list = direction_list(board)
            direction, x, y = dir_list[0], dir_list[1], dir_list[2]
        ship.direction = direction
        print((x,y))
        board.place_ship(ship, (x,y))
#-----------------------------------------------------------------------------
def player_placement(board):
    carrier = Ship(5, "North", "carrier")
    battleship = Ship(4, "North", "battleship")
    submarine = Ship(3, "North", "submarine")
    destroyer = Ship(3, "North", "destroyer")
    cruiser = Ship(2, "North", "cruiser")
    ship_list = [carrier, battleship, submarine, destroyer, cruiser]
    for ship in range(len(ship_list)):
        val = input("Choose a corrdinate to place your {name}".format(name = ship.name))
        cor = get_coords(val)
        direction = input("Choose a direction to orientate the ship: North, South, East, or West")
        while board.legal_placement(ship, cor) == False:
            print("Cannot place a ship there")
            val = input("Choose a new corrdinate to place your {name}".format(name = ship.name))
            cor = get_coords(val)
            direction = input("Choose a new direction to orientate the ship: North, South, East, or West")
        ship.direction = direction
        board.place_ship(ship, cor)


#-----------------------------------------------------------------------------
def play_game():
    public_board = Board(10,10)
    hidden_board = Board(10,10)
    bot_placement(hidden_board)
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
                hidden_board.board[x][y] = "M"
                public_board.board[x][y] = 'M'
                print("Miss!")
                show_board(public_board.board)
        else:
            print("You already fired at that location, choose a different coordinate")
    print("Congrats you win!\nYou sunk all of the enemy ships")
#-----------------------------------------------------------------------------


if __name__ == '__main__':
    play_game()