from matplotlib.style import available
from Board_Class import *
from Ship_Class import *
import random
from graphics import *
import time
from Bot_Class import *
import Helpers as help

#-----------------------------Constants---------------------------------------
player_hidden_board = Board(10,10)
player_guess_board = Board(10,10)
bot_hidden_board = Board(10,10)
bot_guess_board = Board(10,10)

length = 500
width = 500
offset = 50
tx = .5

delta_width = ((width - 2 * offset) / bot_hidden_board.width) 
delta_length = ((length - 2 * offset) / bot_hidden_board.length) 

#-----------------------------------------------------------------------------
def player_placement(board, win, known_rectangles):
    carrier = Ship(5, "North", "carrier")
    battleship = Ship(4, "North", "battleship")
    submarine = Ship(3, "North", "submarine")
    destroyer = Ship(3, "North", "destroyer")
    cruiser = Ship(2, "North", "cruiser")
    ship_list = [carrier, battleship, submarine, destroyer, cruiser]
    direction_list = {(0,-1): "North",
                    (0,1): "South",
                    (1,0): "East",
                    (-1,0): "West"}
    for ship in ship_list:
        help.show_board(board.board)
        # Get Cord
        point = win.getMouse()
        while (point.getX() <= offset or point.getX() >= width - offset
        or point.getY() <= offset or point.getY() >= length - offset):
            point = win.getMouse()
        x = point.getX() - offset
        y = point.getY() - offset
        x = int(x  // delta_width)
        y = int(y  // delta_length)
        cord1 = (x,y)
        help.available_placement(cord1, board, known_rectangles, ship)

        #Get direction
        point = win.getMouse()
        while (point.getX() <= offset or point.getX() >= width - offset
        or point.getY() <= offset or point.getY() >= length - offset):
            point = win.getMouse()
        while ((point.getX() - offset) // delta_width - x, 
        (point.getY() - offset)//delta_length - y) not in direction_list:
            point = win.getMouse()
        x = point.getX() - offset
        y = point.getY() - offset
        x = int(x  // delta_width)
        y = int(y  // delta_length)
        cord2 = (x,y)
        direction = (cord2[0] - cord1[0], cord2[1] - cord1[1])
        direction = direction_list[direction]

        ship.direction = direction
        while board.legal_placement(ship, cord1) == False:
            help.show_ships(board, known_rectangles)

            print("Cannot place a ship there")
            point = win.getMouse()
            while (point.getX() <= offset or point.getX() >= width - offset
            or point.getY() <= offset or point.getY() >= length - offset):
                point = win.getMouse()
            x = point.getX() - offset
            y = point.getY() - offset
            x = int(x  // delta_width)
            y = int(y  // delta_length)
            cord1 = (x,y)
            help.available_placement(cord1, board, known_rectangles, ship)

            #Get direction
            point = win.getMouse()
            while (point.getX() <= offset or point.getX() >= width - offset
            or point.getY() <= offset or point.getY() >= length - offset):
                point = win.getMouse()
            x = point.getX() - offset
            y = point.getY() - offset
            x = int(x  // delta_width)
            y = int(y  // delta_length)
            cord2 = (x,y)
            direction = (cord2[0] - cord1[0], cord2[1] - cord1[1])
            direction = direction_list[direction]


        ship.direction = direction
        board.place_ship(ship, cord1)
        help.show_ships(board, known_rectangles)

    help.show_board(board.board)
#-----------------------------------------------------------------------------
def player_turn(player_guess_board, bot_hidden_board, board_of_rectangles, cord):
    player_guess_board.cords_shot_at.append(cord)
    x,y = cord
    if help.fire(cord, bot_hidden_board):
        bot_hidden_board.board[y][x] = "X"
        player_guess_board.board[y][x] = 'X'
        board_of_rectangles[y][x].setFill('red')
        for ship in bot_hidden_board.ships_on_board:
            if (x,y) in ship.ship_cords:
                ship.hp -= 1
                if ship.hp == 0:
                    print("Hit!")
                    print("You sunk a {name}".format(name = ship.name))
                    for i in ship.ship_cords:
                        x,y = i
                        board_of_rectangles[y][x].setFill('black')
                else:
                    print("Hit!")
        bot_hidden_board.hp -= 1
        help.show_board(player_guess_board.board)
    else:
        bot_hidden_board.board[y][x] = "M"
        player_guess_board.board[y][x] = 'M'
        board_of_rectangles[y][x].setFill('white')
        print("Miss!")
        help.show_board(player_guess_board.board)
#-----------------------------------------------------------------------------
def play_game():

    delta_width = ((width - 2 * offset) / bot_hidden_board.width) 
    delta_length = ((length - 2 * offset) / bot_hidden_board.length) 
    x, y = offset, offset
    p1 = Point(x,y)
    p2 = Point(x + delta_width, y + delta_length)

    guess_board = GraphWin("Guessing Board", width, length)
    known_board = GraphWin("Your Board", width, length)
    guess_board.setBackground("white")
    known_board.setBackground("white")
    guess_rectangles = []
    known_rectangles = []


    for i in range(player_guess_board.length):
        letter = chr(i + 65)
        message = Text(Point(offset//2, y + delta_length//2), letter)
        message2 = Text(Point(offset//2, y + delta_length//2), letter)
        message.setTextColor("black")
        message.draw(guess_board)
        message2.draw(known_board)
        y = y + delta_length


    for i in range(player_guess_board.length):
        num = str(i + 1)
        message = Text(Point(x + delta_width//2, offset//2), num)
        message2 = Text(Point(x + delta_width//2, offset//2), num)
        message.setTextColor("black")
        message.draw(guess_board)
        message2.draw(known_board)
        x = x + delta_width
        

    x, y = offset, offset

    for i in range(bot_hidden_board.length):
        row1 = []
        row2 = []
        for j in range(bot_hidden_board.width):
            r1 = Rectangle(p1,p2)
            r2 = Rectangle(p1,p2)
            r1.setFill("blue")
            r2.setFill("blue")
            row1.append(r1)
            row2.append(r2)
            r1.draw(guess_board)
            r2.draw(known_board)
            x = x + delta_width
            p1 = Point(x,y)
            p2 = Point(x + delta_width, y + delta_length)
        guess_rectangles.append(row1)
        known_rectangles.append(row2)
        x = offset
        y += delta_length
        p1 = Point(x,y)
        p2 = Point(x + delta_width, y + delta_length)

    bot = Bot()
    bot.bot_placement(bot_hidden_board)

    player_placement(player_hidden_board, known_board, known_rectangles)

    for i in range(player_hidden_board.length):
        for j in range(player_hidden_board.width):
            if player_hidden_board.board[i][j] == '1':
                known_rectangles[i][j].setFill("grey")

    help.show_board(bot_hidden_board.board)

    player_cords_shot_at = []
    possible_cords = []
    for i in range(bot_guess_board.length):
            for j in range(bot_guess_board.width):
                possible_cords.append((j, i))

    player_hidden_board.hp = help.get_board_values(player_hidden_board.board)
    bot_hidden_board.hp = help.get_board_values(bot_hidden_board.board)
    rand.shuffle(possible_cords)



# Start of Turn
    turn = 0
    while 0 < player_hidden_board.hp and 0 < bot_hidden_board.hp:
        #Player Turn
        if turn % 2 == 0:
            print("Your turn\n")
            help.show_board(player_guess_board.board)
            print("Click a spot to fire at!\n")
            point = guess_board.getMouse()
            while (point.getX() <= offset or point.getX() >= width - offset
             or point.getY() <= offset or point.getY() >= length - offset):
                point = guess_board.getMouse()
            x = point.getX() - offset
            y = point.getY() - offset
            x = int(x  // delta_width)
            y = int(y  // delta_length)
            cord = (x,y)
            print(cord)
            if cord not in player_guess_board.cords_shot_at:
                player_turn(player_guess_board, bot_hidden_board, guess_rectangles, cord)
                player_cords_shot_at.append(cord)
                x,y = cord
                if bot_hidden_board.board[y][x] == "M":
                    turn += 1
                    print("turn over")
            else:
                print("You've already fired at that location")
            time.sleep(tx)
        #Bot Turn
        else:
            print("The bots turn\n")
            print(bot.destroy_mode)
            print(bot.direction)
            if not bot.destroy_mode:
                print('search')
                x,y = possible_cords[0]
                print("The bot fired at {letter}{number}".format(letter = chr(y+65), number = x+1))
                bot.search(bot_guess_board, player_hidden_board,known_rectangles, possible_cords)
            else:
                print('destroy')
                bot.destroy(bot_guess_board, player_hidden_board,known_rectangles, possible_cords)
                x,y = bot.last_shot
                print("The bot fired at {letter}{number}".format(letter = chr(y+65), number = x+1))
            print("Your board\n")
            help.show_board(player_hidden_board.board)
            time.sleep(tx)
            if player_hidden_board.board[y][x] == "M" :
                    turn += 1
    if player_hidden_board.hp <= 0:
        print("The AI sunk all your ships, you lost")
    elif bot_hidden_board.hp <= 0: 
        print("Congrats you win!\nYou sunk all of the enemy ships")

#-----------------------------------------------------------------------------


if __name__ == '__main__':
    play_game()
