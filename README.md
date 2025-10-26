# Rock, Paper, Scissors (Including Extended Version) 
*A modular, object-oriented Python game.*

## Overview
This is a console-based version of **Rock, Paper, Scissors**, implemented in Python as part of a coding challenge.  
It supports both:
- **Classic version:** Rock, Paper, Scissors  
- **Extended version:** Rock, Paper, Scissors, Lizard, Spock  

The project demonstrates **clean code structure**, **object-oriented programming**, and **modular design principles**.

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

Method
Description
game_play()
Runs the main loop and controls gameplay flow
game_setup()
Initializes scores, rounds, and mode
choose_version()
Lets the player choose between classic and extended mode
get_user_choice()
Handles player input validation
get_computer_choice()
Generates computer’s random move
evaluate_round()
Compares choices and updates scores
check_end_condition()
Determines when the game should end
game_end()
Displays the final results