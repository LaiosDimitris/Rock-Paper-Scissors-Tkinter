import unittest
import game 

gametest = game.Game(10)

class GameTesting(unittest.TestCase):

    def test_user_move_setter_and_getter(self):
        for move in ['rock', 'paper', 'scissors']:
            gametest.set_user_move(move)
            self.assertEqual(gametest.get_user_move(), move, msg=f"User move needs to be '{move}'.")

    def test_user_score_setter_and_getter(self):
        for i in range(10):
            gametest.set_user_score(i)
            self.assertEqual(gametest.get_user_score(), i, msg=f"User score needs to be {i}.")

    def test_computer_move_setter_and_getter(self):
        gametest.set_computer_move()
        self.assertIn(gametest.get_computer_move(), ['rock', 'paper', 'scissors'], msg=f"Computer move needs to be '{['rock', 'paper', 'scissors']}'.")

    def test_computer_score_setter_and_getter(self):
        for i in range(10):
            gametest.set_computer_score(i)
            self.assertEqual(gametest.get_computer_score(), i, msg=f"Computer score needs to be {i}.")

    def test_round_winner(self):
        gametest.set_user_move('rock')

        gametest.computer['move'] = 'rock'
        self.assertEqual(gametest.get_round_winner(), 'draw', msg="Result needs to be 'draw'.")
        gametest.computer['move'] = 'paper'
        self.assertEqual(gametest.get_round_winner(), 'computer', msg="Result needs to be 'computer'.")
        gametest.computer['move'] = 'scissors'
        self.assertEqual(gametest.get_round_winner(), 'user', msg="Result needs to be 'user'.")

        gametest.set_user_move('paper')

        gametest.computer['move'] = 'rock'
        self.assertEqual(gametest.get_round_winner(), 'user', msg="Result needs to be 'user'.")
        gametest.computer['move'] = 'paper'
        self.assertEqual(gametest.get_round_winner(), 'draw', msg="Result needs to be 'draw'.")
        gametest.computer['move'] = 'scissors'
        self.assertEqual(gametest.get_round_winner(), 'computer', msg="Result needs to be 'computer'.")

        gametest.set_user_move('scissors')

        gametest.computer['move'] = 'rock'
        self.assertEqual(gametest.get_round_winner(), 'computer', msg="Result needs to be 'computer'.")
        gametest.computer['move'] = 'paper'
        self.assertEqual(gametest.get_round_winner(), 'user', msg="Result needs to be 'user'.")
        gametest.computer['move'] = 'scissors'
        self.assertEqual(gametest.get_round_winner(), 'draw', msg="Result needs to be 'draw'.")

    def test_game_winner(self):
        gametest.set_user_score(10)
        gametest.set_computer_score(0)
        self.assertEqual(gametest.get_game_winner(), 'user', msg="Result needs to be 'user'.")

        gametest.set_user_score(0)
        gametest.set_computer_score(10)
        self.assertEqual(gametest.get_game_winner(), 'computer', msg="Result needs to be 'computer'.")

        gametest.set_user_score(10)
        gametest.set_computer_score(10)
        self.assertEqual(gametest.get_game_winner(), 'draw', msg="Result needs to be 'draw'.")



if __name__ == "__main__":
    unittest.main()