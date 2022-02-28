import random


#-----------------------------------------------------------------------------
def fire(cor, board):
    x,y = cor
    if board.board[y][x] == '1':
        return True
    else:
        return False
#-----------------------------------------------------------------------------
#take ship length
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

