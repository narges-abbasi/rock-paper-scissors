import random
from data import RULES

class Game:
    # Game initialization and evaluation
    def game_play(self, player1, player2) -> None:
        p1_score, p2_score, rounds, options, end_condition = self.game_setup()

        while True:
            p1_choice = player1.get_choice(options)
            p2_choice = player2.get_choice(options)

            print(f"{player1.name} chose: {p1_choice}, {player2.name} chose: {p2_choice}")

            p1_score, p2_score, rounds = self.evaluate_round(
                player1_choice=p1_choice,
                player2_choice=p2_choice,
                player1_score=p1_score,
                player2_score=p2_score, rounds=rounds)

            print(f"Scores: {player1.name}: {p1_score}, {player2.name}: {p2_score}")

            if self.check_end_condition(end_condition, rounds, p1_score, p2_score):
                break

        self.game_end(p1_score, p2_score)
    
    def game_setup(self) -> tuple:
        p1_score = 0
        p2_score= 0
        rounds = 0

        options = self.choose_version()

        conditions = ["Best Out of Three Rounds", "First With Five Points"]

        while True:
            end_condition = input(f"How should the game end? (choose (1) for: {conditions[0]}, (2) for: {conditions[1]})")
            if end_condition in ["1", "2"]:
                break
            print("Invalid choice! Please enter 1 or 2")
        return p1_score, p2_score, rounds, options, end_condition

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


    # Comparison and update score
    def evaluate_round(self, player1_choice: str, player2_choice: str, player1_score: int, player2_score: int, rounds: int) -> tuple:
        if player1_choice == player2_choice:
            print("It's a draw!")
        elif player2_choice in RULES[player1_choice]:
            print("You win this round!")
            player1_score += 1 
            rounds += 1
        else:
            print("Computer wins this round!")
            player2_score += 1
            rounds += 1

        return player1_score, player2_score, rounds 
    
    def check_end_condition(self, user_condition: str, rounds: int, user_score: int, computer_score: int) -> bool:
        if user_condition == "1":
            if user_score == 2 or computer_score == 2:
                return True
        if user_condition == "2":
            if user_score == 5 or computer_score == 5:
                return True
        return False

    def game_end(self, player1_score: int, player2_score: int) -> None:
        print("-------------------------------------------------------------------")
        print("Game is Over!")
        if player1_score > player2_score:
            print(f"You won the game ({player1_score} - {player2_score})")
        elif player2_score > player1_score:
            print(f"Computer won the game ({player2_score} - {player1_score})")
        else:
            print(f"It's a draw!({player2_score} - {player1_score})")
