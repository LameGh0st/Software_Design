from Board_Class import *
from Ship_Class import *
import random


#-----------------------------------------------------------------------------
def get_coords(cord):
    letter = cord[0]
    num = cord[1:]
    return (int(num)-1,ord(letter)-65)
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
def Fire(cor, board):
    x,y = cor
    if board.board[y][x] == '1':
        return True
    else:
        return False
#-----------------------------------------------------------------------------
#take ship length
def direction_list(board):
    direction_list = ["North", "South", "East", "West"]
    direction = random.choice(direction_list)
    x = random.randrange(0, board.width)
    y = random.randrange(0, board.length)
    return [direction, x, y]
#-----------------------------------------------------------------------------
def bot_placement(board):
    carrier = Ship(5, "North", "carrier")
    battleship = Ship(4, "North", "battleship")
    submarine = Ship(3, "North", "submarine")
    destroyer = Ship(3, "North", "destroyer")
    cruiser = Ship(2, "North", "curiser")
    ship_list = [carrier, battleship, submarine, destroyer, cruiser]
    for ship in ship_list:
        direction, x, y = direction_list(board)
        ship.direction = direction
        while board.legal_placement(ship, (x,y)) == False:
            direction, x, y = direction_list(board)
            ship.direction = direction
        ship.direction = direction
        board.place_ship(ship, (x,y))
#-----------------------------------------------------------------------------
def player_placement(board):
    carrier = Ship(5, "North", "carrier")
    battleship = Ship(4, "North", "battleship")
    submarine = Ship(3, "North", "submarine")
    destroyer = Ship(3, "North", "destroyer")
    cruiser = Ship(2, "North", "cruiser")
    ship_list = [carrier, battleship, submarine, destroyer, cruiser]
    for ship in ship_list:
        show_board(board.board)
        val = input("Choose a corrdinate to place your {name}\n".format(name = ship.name))
        cor = get_coords(val)
        direction = input("Choose a direction to orientate the ship: North, South, East, or West\n")
        ship.direction = direction
        while board.legal_placement(ship, cor) == False:
            print("Cannot place a ship there")
            val = input("Choose a new corrdinate to place your {name}\n".format(name = ship.name))
            cor = get_coords(val)
            direction = input("Choose a new direction to orientate the ship: North, South, East, or West\n")
            ship.direction = direction
        ship.direction = direction
        board.place_ship(ship, cor)
    show_board(board.board)
#-----------------------------------------------------------------------------
def bot_turn(bot_guess_board, player_hidden_board, cords):
    cord = cords[0] 
    x,y = cord
    if Fire(cord, player_hidden_board):
        bot_guess_board.board[y][x] = 'X'
        player_hidden_board.board[y][x] = 'X'
        bot_guess_board.cords_shot_at.append(cord)
        for ship in bot_guess_board.ships_on_board:
                    if (x,y) in ship.ship_cords:
                        ship.hp -= 1
                        if ship.hp == 0:
                            print("Hit!")
                            print("The AI sunk a ship!")
                        else:
                            print("Hit!")
        player_hidden_board.hp
        show_board(bot_guess_board.board)
    else:
        bot_guess_board.board[y][x] = 'M'
        player_hidden_board.board[y][x] = 'M'
        bot_guess_board.cords_shot_at.append(cord)
        print('Miss')
        show_board(bot_guess_board.board)
#-----------------------------------------------------------------------------
def player_turn(player_guess_board, bot_hidden_board, cord):
    player_guess_board.cords_shot_at.append(cord)
    x,y = cord
    if Fire(cord, bot_hidden_board):
        bot_hidden_board.board[y][x] = "X"
        player_guess_board.board[y][x] = 'X'
        for ship in bot_hidden_board.ships_on_board:
            if (x,y) in ship.ship_cords:
                ship.hp -= 1
                if ship.hp == 0:
                    print("Hit!")
                    print("You sunk a {name}".format(name = ship.name))
                else:
                    print("Hit!")
        bot_hidden_board.hp -= 1
        show_board(player_guess_board.board)
    else:
        bot_hidden_board.board[y][x] = "M"
        player_guess_board.board[y][x] = 'M'
        print("Miss!")
        show_board(player_guess_board.board)
#-----------------------------------------------------------------------------
def play_game():
    player_hidden_board = Board(10,10)
    player_guess_board = Board(10,10)
    bot_hidden_board = Board(10,10)
    bot_guess_board = Board(10,10)

    

    bot_placement(bot_hidden_board)

    player_placement(player_hidden_board)

    show_board(bot_hidden_board.board)

    player_cords_shot_at = []
    possible_cords = []
    for i in range(bot_guess_board.length):
            for j in range(bot_guess_board.width):
                possible_cords.append((j, i))

    player_hidden_board.hp = get_board_values(player_hidden_board.board)
    bot_hidden_board.hp = get_board_values(bot_hidden_board.board)
    rand.shuffle(possible_cords)




    turn = 0
    while 0 < player_hidden_board.hp and 0 < bot_hidden_board.hp:
        if turn % 2 == 0:
            print("Your turn\n")
            show_board(player_guess_board.board)
            val = input("Choose a coordinate to fire at!\n")
            cord = get_coords(val)
            if cord not in player_guess_board.cords_shot_at:
                player_turn(player_guess_board, bot_hidden_board, cord)
                player_cords_shot_at.append(cord)
                turn += 1
                print("turn over")
            else:
                print("You've already fired at that location")
        else:
            print("The bots turn\n")
            x,y = possible_cords[0]
            print("The bot fired at {letter}{number}".format(letter = chr(y+65), number = x+1))
            bot_turn(bot_guess_board, player_hidden_board, possible_cords)
            print("Your board\n")
            show_board(player_hidden_board.board)
            possible_cords = possible_cords[1:]
            turn += 1
    if player_hidden_board.hp <= 0:
        print("The AI sunk all your ships, you lost")
    elif bot_hidden_board.hp <= 0: 
        print("Congrats you win!\nYou sunk all of the enemy ships")

#-----------------------------------------------------------------------------


if __name__ == '__main__':
    play_game()