import unittest
from game import Game
from data import RULES

# To verify that evaluate_round() works as expected
class TestEvaluateRound(unittest.TestCase):

    game_test = Game()

    def test_player_wins(self):
        player_score, computer_score, rounds = self.game_test.evaluate_round(
            player_choice="rock",
            computer_choice="scissors",
            player_score=0,
            computer_score=0,
            rounds=0
        )

        self.assertEqual(player_score, 1)
        self.assertEqual(computer_score, 0)
        self.assertEqual(rounds, 1)

    def test_computer_wins(self):
        player_score, computer_score, rounds = self.game_test.evaluate_round(
            player_choice="scissors",
            computer_choice="rock",
            player_score=0,
            computer_score=0,
            rounds=0
        )

        self.assertEqual(player_score, 0)
        self.assertEqual(computer_score, 1)
        self.assertEqual(rounds, 1)

    def test_draw_round(self):
        player_score, computer_score, rounds = self.game_test.evaluate_round(
            player_choice="rock",
            computer_choice="rock",
            player_score=1,
            computer_score=1,
            rounds=3
        )

        self.assertEqual(player_score, 1)
        self.assertEqual(computer_score, 1)
        self.assertEqual(rounds, 3)


if __name__ == "__main__":
    unittest.main()


