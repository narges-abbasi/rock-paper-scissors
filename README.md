# Rock, Paper, Scissors (Including Extended Version) 
*A modular, object-oriented Python game.*



## Overview
This is a console-based version of **Rock, Paper, Scissors**, implemented in Python as part of a coding challenge.  
It supports both:
- **Classic version:** Rock, Paper, Scissors  
- **Extended version:** Rock, Paper, Scissors, Lizard, Spock  



## Features
- **Clean Code Structure**
- **Modular Design**
- **Flexible Rules for Future Expansion**



## Core Components

### data.py
Contains the game’s rules dictionary which is expandable:
```python
RULES = {
    "scissors": ["paper","lizard"],
    "paper": ["rock","spock"],
    "rock": ["scissors","lizard"],
    "lizard": ["paper","spock"],
    "spock": ["scissors","rock"]
}
```


### Game.py
Defines the Game class with all the main gameplay logic:

game_play(): Runs the main loop and controls gameplay flow.

game_setup(): Initializes scores, rounds, and game version(classic or extended).

choose_version(): Lets the player choose between classic and extended versions.

get_user_choice(): Gets player's input and validate it.

get_computer_choice(): Generates computer’s random choice.

evaluate_round(): Compares choices and updates scores.

check_end_condition(): Checks whether the game should end or not.

game_end(): Displays the final results.



### main.py
Serves as the **enty point** of the program by calling game_play() method.


## Future Improvements
- Create a GUI Version
- Include Timing
- Consider Multithreading