from random import *
from Bot_Class import *
from Smarter_Bot_Class import *
import Helpers as help
from pip import main

def tournament(players, number_of_games):
    player1 = players[0]
    player2 = players[1]

    player1_wins = 0
    player2_wins = 0

    #Start of tournament/setting start variables for each game
    for i in range(number_of_games):
        print("game {}.".format(i))
        player1.reset()
        player2.reset()
        player1.placement()
        player2.placement()
        player1.hidden_board.hp = help.get_board_values(player1.hidden_board.board)
        player2.hidden_board.hp = help.get_board_values(player2.hidden_board.board)

        #randomly choose starting player then start game loop
        player_number = random.choice([0,1])
        while True:
            player = players[player_number]
            other_player = players[1-player_number]
            cord = player.move(None)

            #Give move to other player to get hit/miss/sink
            data  = other_player.lookup(cord)
            result = data[0]
            sunk_ship_cords = data[1]
            sunk_ship_length = data[2]

            
            #update guess board and any other variables
            player.process(cord, result, sunk_ship_cords, sunk_ship_length)

            if result == "Game Over":
                break
            if result == "Miss":
                player_number = 1 - player_number
        if player1.hidden_board.hp <= 0:
            player2_wins += 1
        elif player2.hidden_board.hp <= 0:
            player1_wins += 1
            
    print("Out of {} games, player1 won {} with a winrate of {}".format(
        number_of_games, player1_wins, (player1_wins / number_of_games) * 100
    ))
    print("Out of {} games, player2 won {} with a winrate of {}".format(
        number_of_games, player2_wins, (player2_wins / number_of_games) * 100
    ))


if __name__ == '__main__':
    tournament([Bot(), Smarter_Bot()], 100)
