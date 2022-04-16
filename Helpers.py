import random
from graphics import *
from pip import main
 

#-----------------------------------------------------------------------------
def fire(cor, Board):
    x,y = cor
    if Board.board[y][x] == '1':
        return True
    else:
        return False
#-----------------------------------------------------------------------------
def direction_list(Board):
    direction_list = ["North", "South", "East", "West"]
    direction = random.choice(direction_list)
    x = random.randrange(0, Board.width)
    y = random.randrange(0, Board.length)
    return [direction, x, y]
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
def get_board_values(board):
    sum = 0
    for i in range(len(board)):
        for j in board[i]:
            sum += int(j)
    return sum
#-----------------------------------------------------------------------------
def available_placement(cord, board, known_rectangles, ship):
    x = cord[0]
    y = cord[1]
    known_rectangles[y][x].setFill("grey")

    ship.direction = "West"
    if x != 0 and board.legal_placement(ship, (x,y)):
        for i in range(ship.size-1):
            known_rectangles[y][x-1-i].setFill("yellow")
    
    ship.direction = "North"
    if y != 0 and board.legal_placement(ship, (x,y)):
        for i in range(ship.size-1):
            known_rectangles[y-1-i][x].setFill("yellow")

    ship.direction = "South"
    if y < board.length - 1 and y >= 0 and board.legal_placement(ship, (x,y)):
        for i in range(ship.size-1):
            known_rectangles[y+1+i][x].setFill("yellow")

    ship.direction = "East"
    if x < board.width - 1 and x >= 0 and board.legal_placement(ship, (x,y)):
        for i in range(ship.size-1):
            known_rectangles[y][x+1+i].setFill("yellow")
#-------------------------------------------------------------------------------
def show_ships(board, known_rectangles):
        for i in range(board.length):
            for j in range(board.width):
                if board.board[i][j] == '1':
                    known_rectangles[i][j].setFill("grey")
                if board.board[i][j] == '0':
                    known_rectangles[i][j].setFill("blue")
#-------------------------------------------------------------------------------
def legal_shot(Board, cord):
    x,y = cord
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= Board.width:
        return False
    if y >= Board.length:
        return False
    if Board.board[y][x] != '0':
        return False
    if (x,y) in Board.cords_shot_at:
        return False
    else:
        return True
#------------------------------------------------------------------------------
def update_graphics(cord, result, hidden_board, win_rec):
    x, y = cord
    if result == "Hit":
        win_rec[y][x].setFill('red')
    if result == "Sunk":
        for ship in hidden_board.ships_on_board:
            if (x,y) in ship.ship_cords:
                for i in ship.ship_cords:
                    x,y = i
                    win_rec[y][x].setFill('black')
    if result == "Miss":
        win_rec[y][x].setFill('white')
