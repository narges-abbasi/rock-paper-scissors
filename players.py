from abc import ABC, abstractmethod
import random
class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    @abstractmethod
    def get_choice(self, options: list[str]) -> str:
        pass
    
class HumanPlayer(Player):
    def get_choice(self, options: list[str]) -> str:
        while True:
            choice = input(f"choose from {options}:").lower()
            if choice not in options:
                print("Invalid chioce! Please try again")
                continue
            return choice

class ComputerPlayer(Player):
    def get_choice(self, options: list[str]) -> str:
        return random.choice(options)

class PredictablePlayer(Player):
    #override the method for a player with a fixed choice (scissors)
    pass


