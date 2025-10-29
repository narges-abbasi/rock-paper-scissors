from game import Game
from players import HumanPlayer, ComputerPlayer

def main() -> None:
    print("Welcome to Rock, Paper, Scissors Game!")

    player1 = HumanPlayer("You")
    player2 = ComputerPlayer("Computer")

    game = Game()
    game.game_play(player1=player1, player2=player2)

if __name__ == "__main__":
    main()
