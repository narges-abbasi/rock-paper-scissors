import random
from data import RULES

class Game:
    # Game initialization and evaluation
    def game_play(self) -> None:
        user_score, computer_score, rounds, options, user_condition = self.game_setup()

        while True:
            user_choice = self.get_user_choice(options)
            computer_choice = self.get_computer_choice(options)

            print(f"You chose: {user_choice} \n Computer chose: {computer_choice}")

            user_score, computer_score, rounds = self.evaluate_round(
                player_choice=user_choice,
                computer_choice=computer_choice,
                player_score=user_score,
                computer_score=computer_score, rounds=rounds)

            print(f"Your score: {user_score}\n Computer's score: {computer_score}")

            if self.check_end_condition(user_condition, rounds, user_score, computer_score):
                break

        self.game_end(user_score, computer_score)
    
    def game_setup(self) -> tuple:
        user_score = 0
        computer_score = 0
        rounds = 0

        options = self.choose_version()

        conditions = ["Best Out of Three Rounds", "First With Five Points"]

        while True:
            user_condition = input(f"How should the game end? (choose (1) for: {conditions[0]}, (2) for: {conditions[1]})")
            if user_condition in ["1", "2"]:
                break
            print("Invalid choice! Please enter 1 or 2")
        return user_score, computer_score, rounds, options, user_condition

    # Classic vs Extended Versions
    def choose_version(self) -> list[str]:

        while True:
            version = input("Do you want to play the classic (1) or extended (2) version?")
            if version == "1":
                return ["scissors", "paper", "rock"]
            elif version == "2":
                return list(RULES.keys())
            else:
                print("Invalid choice! Please enter 1 or 2")

    def get_user_choice(self, options: list[str]) -> str:
        while True:
            user_choice = input(f"choose from {options}:").lower()
            if user_choice not in options:
                print("Invalid chioce! Please try again")
                continue
            return user_choice

    def get_computer_choice(self, options: list[str]) -> str:
        computer_choice = random.choice(options)
        return computer_choice

    # Comparison and update score
    def evaluate_round(self, player_choice: str, computer_choice: str, player_score: int, computer_score: int, rounds: int) -> tuple:
        if player_choice == computer_choice:
            print("It's a draw!")
        elif computer_choice in RULES[player_choice]:
            print("You win this round!")
            player_score += 1 
            rounds += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            rounds += 1

        return player_score, computer_score, rounds 
    
    def check_end_condition(self, user_condition: str, rounds: int, user_score: int, computer_score: int) -> bool:
        if user_condition == "1":
            if user_score == 2 or computer_score == 2:
                return True
        if user_condition == "2":
            if user_score == 5 or computer_score == 5:
                return True
        return False

    def game_end(self, user_score: int, computer_score: int) -> None:
        print("-------------------------------------------------------------------")
        print("Game is Over!")
        if user_score > computer_score:
            print(f"You won the game ({user_score} - {computer_score})")
        elif computer_score > user_score:
            print(f"Computer won the game ({computer_score} - {user_score})")
        else:
            print(f"It's a draw!({computer_score} - {user_score})")
