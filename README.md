# **Software Design**

## Playing Battleship
    * To play the battleship program run the Play_Battleship file
    * Two GUI board will appear on your screen, one titled "Your Board" and another titled "Guess Board"
    * On "Your Board" click any coordinate you would like to place your first ship. Ships will always be placed in order from largest to smallest
    * After clicking an initial coordinate, all adjecent tiles will turn yellow, click one of them to determine the direction the ship will be placed.
    * If a placement is invalid your initial click will dissapear along with the yellow tiles, choose a new starting location and proceed as normal.
    * After all ships have been placed click on any coordinate on "Guess Board" to fire at the opponent
    * You and the computer will then take turns firing at one another until either of you have sunk all the others ships




## Short Term Goals
    * Clean up code
    * rewrite repetitive code as helper functions

## Medium Term Goals
    * Turn the bot turn and placement into a class
    * Create a sligthly smarter bot class to play agaisnt
    * Create a GA bot to play against

## Long Term Goals
    * Create Nueral Network bot to play
    * Make a heat map with statistacal probability to determine firing spot

## Stretch Goals
    * allow for other moves, such as a scatter-shot(Possibly a point system for different moves)
    * How does strategy change if you keep firing when you hit a ship until you miss