from matplotlib.style import available
from Board_Class import *
from Ship_Class import *
import random
from graphics import *
import time
from Bot_Class import *
import Helpers as help
import Constants as cons
from Player_Class import *


#-----------------------------------------------------------------------------
def play_game():

    delta_width = ((cons.width - 2 * cons.offset) / cons.bot_hidden_board.width) 
    delta_length = ((cons.length - 2 * cons.offset) / cons.bot_hidden_board.length) 
    x, y = cons.offset, cons.offset
    p1 = Point(x,y)
    p2 = Point(x + delta_width, y + delta_length)

    guess_board = GraphWin("Guessing Board", cons.width, cons.length)
    known_board = GraphWin("Your Board", cons.width, cons.length)
    guess_board.setBackground("white")
    known_board.setBackground("white")
    guess_rectangles = []
    known_rectangles = []


    for i in range(cons.player_guess_board.length):
        letter = chr(i + 65)
        message = Text(Point(cons.offset//2, y + delta_length//2), letter)
        message2 = Text(Point(cons.offset//2, y + delta_length//2), letter)
        message.setTextColor("black")
        message.draw(guess_board)
        message2.draw(known_board)
        y = y + delta_length


    for i in range(cons.player_guess_board.length):
        num = str(i + 1)
        message = Text(Point(x + delta_width//2, cons.offset//2), num)
        message2 = Text(Point(x + delta_width//2, cons.offset//2), num)
        message.setTextColor("black")
        message.draw(guess_board)
        message2.draw(known_board)
        x = x + delta_width
        

    x, y = cons.offset, cons.offset

    for i in range(cons.bot_hidden_board.length):
        row1 = []
        row2 = []
        for j in range(cons.bot_hidden_board.width):
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
        x = cons.offset
        y += delta_length
        p1 = Point(x,y)
        p2 = Point(x + delta_width, y + delta_length)

    bot = Bot()
    bot.bot_placement(cons.bot_hidden_board)

    player = Player()
    player.player_placement(cons.player_hidden_board, known_board, known_rectangles)

    for i in range(cons.player_hidden_board.length):
        for j in range(cons.player_hidden_board.width):
            if cons.player_hidden_board.board[i][j] == '1':
                known_rectangles[i][j].setFill("grey")

    help.show_board(cons.bot_hidden_board.board)

    player_cords_shot_at = []
    possible_cords = []
    for i in range(cons.bot_guess_board.length):
            for j in range(cons.bot_guess_board.width):
                possible_cords.append((j, i))

    cons.player_hidden_board.hp = help.get_board_values(cons.player_hidden_board.board)
    cons.bot_hidden_board.hp = help.get_board_values(cons.bot_hidden_board.board)
    rand.shuffle(possible_cords)



# Start of Turn
    turn = 0
    while 0 < cons.player_hidden_board.hp and 0 < cons.bot_hidden_board.hp:
        #Player Turn
        if turn % 2 == 0:
            print("Your turn\n")
            help.show_board(cons.player_guess_board.board)
            print("Click a spot to fire at!\n")
            point = guess_board.getMouse()
            while (point.getX() <= cons.offset or point.getX() >= cons.width - cons.offset
             or point.getY() <= cons.offset or point.getY() >= cons.length - cons.offset):
                point = guess_board.getMouse()
            x = point.getX() - cons.offset
            y = point.getY() - cons.offset
            x = int(x  // delta_width)
            y = int(y  // delta_length)
            cord = (x,y)
            if cord not in cons.player_guess_board.cords_shot_at:
                player.player_turn(cons.player_guess_board, cons.bot_hidden_board, guess_rectangles, cord)
                player_cords_shot_at.append(cord)
                x,y = cord
                if cons.bot_hidden_board.board[y][x] == "M":
                    turn += 1
                    print("turn over")
            else:
                print("You've already fired at that location")
            time.sleep(cons.tx)
        #Bot Turn
        else:
            print("The bots turn\n")
            if not bot.destroy_mode:
                x,y = possible_cords[0]
                print("The bot fired at {letter}{number}".format(letter = chr(y+65), number = x+1))
                bot.search(cons.bot_guess_board, cons.player_hidden_board,known_rectangles, possible_cords)
            else:
                bot.destroy(cons.bot_guess_board, cons.player_hidden_board,known_rectangles, possible_cords)
                x,y = bot.last_shot
                print("The bot fired at {letter}{number}".format(letter = chr(y+65), number = x+1))
            print("Your board\n")
            help.show_board(cons.player_hidden_board.board)
            time.sleep(cons.tx)
            if cons.player_hidden_board.board[y][x] == "M" :
                    turn += 1
    if cons.player_hidden_board.hp <= 0:
        print("The AI sunk all your ships, you lost")
    elif cons.bot_hidden_board.hp <= 0: 
        print("Congrats you win!\nYou sunk all of the enemy ships")

#-----------------------------------------------------------------------------


if __name__ == '__main__':
    play_game()
