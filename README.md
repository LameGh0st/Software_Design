# **Software Design**


## Summary 
This project is a recreation of the game Battleship. It allows for a human to play against a computer player, with the goal being to make many different bots that use different strategies ot try to find one that can consitently beat human players. I made two different bot classes for the human player to play against, and a file called tournament which allows two bots to automatically play games against eachother for testing purposes and data collecting. Given more time I would abstract the graphics code more so Play_Battleship had the option to turn them on or off. I would also create a couple of new bots that use different strategies, such as shooting in the middle of the largest area left, or creating a genetic algorithm.

## Bugs
    * Currently the Smarter_Bot() player will randomly get stuck in an infinite loop. This bug seems to be random and rare as it has only ever been seen while playing another bot for many games in a row in the tournament function.
    * If Smarter_Bot() hits a ship and hit it again to find which direction it's going, it is supposed to shoot in the exact opposite direction if it misses. (i.e. If it hits north then misses it should then shoot south of the original hit). This does not always seem to happen

## List of Files
    * graphics.py (Zelle's graphic library to create interactive boards)
    * AbstractPlayer.py (Parent for all other players so they can inherit methods)
    * Board_Class.py (Creates Board object for player to play on)
    * Bot_Class.py (Simplest bot that fires randomly and can always sink a ship that it has hit)
    * Constants.py (Constant variables to control how the graphics window is made)
    * Helpers.py (Library of helper functions for the game loops and player classes to use)
    * HumanPlayer_Class.py ()
    * Play_Battleship.py
    * Ship_Class.py
    * Smarter_Bot_Class.py
    * tournament.py


## Playing Battleship
    * To play the battleship program run the Play_Battleship file
    * Two GUI board will appear on your screen, one titled "Your Board" and another titled "Guess Board"
    * On "Your Board" click any coordinate you would like to place your first ship. Ships will always be placed in order from largest to smallest
    * After clicking an initial coordinate, all adjecent tiles will turn yellow, click one of them to determine the direction the ship will be placed.
    * If a placement is invalid your initial click will dissapear along with the yellow tiles, choose a new starting location and proceed as normal.
    * After all ships have been placed click on any coordinate on "Guess Board" to fire at the opponent
    * If a tile turns white then the shot missed, if it turns red then it was a hit. When a ship is fully sunk all the tiles will turn black
    * You and the computer will then take turns firing at one another until either of you have sunk all the others ships




