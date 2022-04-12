from matplotlib.style import available
from Board_Class import *
from Ship_Class import *
from graphics import *
import time
from Bot_Class import *
import Helpers as help
import Constants as cons
from HumanPlayer_Class import *

#-----------------------------------------------------------------------------
def play_game():

    bot = Bot()
    human = HumanPlayer()

    
    x, y = cons.offset, cons.offset
    p1 = Point(x,y)
    p2 = Point(x + cons.delta_width, y + cons.delta_length)

    win_guess_board = GraphWin("Guessing Board", cons.width, cons.length)
    win_known_board = GraphWin("Your Board", cons.width, cons.length)
    win_guess_board.setBackground("white")
    win_known_board.setBackground("white")
    guess_rectangles = []
    known_rectangles = []


    for i in range(human.guess_board.length):
        letter = chr(i + 65)
        message = Text(Point(cons.offset//2, y + cons.delta_length//2), letter)
        message2 = Text(Point(cons.offset//2, y + cons.delta_length//2), letter)
        message.setTextColor("black")
        message.draw(win_guess_board)
        message2.draw(win_known_board)
        y = y + cons.delta_length


    for i in range(human.guess_board.length):
        num = str(i + 1)
        message = Text(Point(x + cons.delta_width//2, cons.offset//2), num)
        message2 = Text(Point(x + cons.delta_width//2, cons.offset//2), num)
        message.setTextColor("black")
        message.draw(win_guess_board)
        message2.draw(win_known_board)
        x = x + cons.delta_width
        

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
            r1.draw(win_guess_board)
            r2.draw(win_known_board)
            x = x + cons.delta_width
            p1 = Point(x,y)
            p2 = Point(x + cons.delta_width, y + cons.delta_length)
        guess_rectangles.append(row1)
        known_rectangles.append(row2)
        x = cons.offset
        y += cons.delta_length
        p1 = Point(x,y)
        p2 = Point(x + cons.delta_width, y + cons.delta_length)

    bot.placement()
    human.placement(win_known_board, known_rectangles)

    for i in range(human.hidden_board.length):
        for j in range(human.hidden_board.width):
            if human.hidden_board.board[i][j] == '1':
                known_rectangles[i][j].setFill("grey")

    help.show_board(cons.bot_hidden_board.board)


    players = [bot, human]
    guess_boards = [bot.guess_board, human.guess_board]
    win_boards = [win_known_board, win_guess_board]
    hidden_boards = [bot.hidden_board, human.hidden_board]
    rectangles = [known_rectangles, guess_rectangles]
    players[0].hidden_board.hp = help.get_board_values(human.hidden_board.board)
    players[1].hidden_board.hp = help.get_board_values(bot.hidden_board.board)

    print(players[0].hidden_board.hp)
    print(players[1].hidden_board.hp)


# Start of Game
    player_number = 0 #random.choice([0,1])
    while 0 < players[0].hidden_board.hp and 0 < players[1].hidden_board.hp:
        player = players[player_number]
        guess_board = guess_boards[player_number]
        hidden_board = hidden_boards[1-player_number]
        win_board = win_boards[player_number]
        cord = player.move(win_board)
        win_rec = rectangles[player_number]
        if cord not in guess_board.cords_shot_at:
            guess_board.cords_shot_at.append(cord)
            x,y = cord
            if help.fire(cord, hidden_board):
                hidden_board.board[y][x] = "X"
                guess_board.board[y][x] = 'X'
                win_rec[y][x].setFill('red')
                for ship in hidden_board.ships_on_board:
                    if (x,y) in ship.ship_cords:
                        ship.hp -= 1
                        if ship.hp == 0:
                            print("Hit!")
                            print("You sunk a {name}".format(name = ship.name))
                            for i in ship.ship_cords:
                                x,y = i
                                win_rec[y][x].setFill('black')
                        else:
                            print("Hit!")
                hidden_board.hp -= 1
                time.sleep(cons.tx)
            else:
                print("Miss")
                hidden_board.board[y][x] = 'M'
                guess_board.board[y][x] = 'M'
                win_rec[y][x].setFill("white")
                player_number = 1-player_number
                print("turn over")
                time.sleep(cons.tx)
        else:
            print("You've already fired at that location")
    
    if cons.player_hidden_board.hp <= 0:
        print("The AI sunk all your ships, you lost")
    elif cons.bot_hidden_board.hp <= 0: 
        print("Congrats you win!\nYou sunk all of the enemy ships")

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    play_game()
