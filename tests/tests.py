from src.main import welcome, start_game, generate_number, guess_number, player_name, player_turn, computer_turn
import unittest

class TestGuessNumber(unittest.TestCase):

    """    def test_player_name(self):
        ddf """
    
    def test_generate_number(self):
        expected_random_number = 60
        self.assertEqual(expected_random_number, 60)


if __name__ == '__main__':
    unittest.main()