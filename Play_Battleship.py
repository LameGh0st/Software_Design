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
    win_boards = [win_known_board, win_guess_board]
    rectangles = [known_rectangles, guess_rectangles]
    players[0].hidden_board.hp = help.get_board_values(human.hidden_board.board)
    players[1].hidden_board.hp = help.get_board_values(bot.hidden_board.board)

# Start of Game
    player_number = random.choice([0,1])
    while True:
        player = players[player_number]
        other_player = players[1-player_number]
        win_board = win_boards[player_number]
        win_rec = rectangles[player_number]

        #player makes their move
        cord = player.move(win_board)

        #Give move to other player to get hit/miss/sink
        result, sunk_ship_cords = other_player.lookup(cord)
        
        #update guess board and any other variables
        player.process(cord, result, sunk_ship_cords)

        #update graphics
        help.update_graphics(cord, result, other_player.hidden_board, win_rec)
        time.sleep(cons.tx)
        if result == "Game Over":
            break
        if result == "Miss":
            player_number = 1 - player_number

        
    if players[1].hidden_board.hp <= 0:
        print("The AI sunk all your ships, you lost")
    elif players[0].hidden_board.hp <= 0: 
        print("Congrats you win!\nYou sunk all of the enemy ships")

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    play_game()
