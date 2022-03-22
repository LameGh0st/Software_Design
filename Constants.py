from Board_Class import *

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