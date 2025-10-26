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
Contains the game’s rule dictionary:
```python
RULES = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "rock": ["scissors", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["scissors", "rock"]
}