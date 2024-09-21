from main import welcome, player_name, generate_number, player_turn, computer_turn, guess_number, validate_guess, tries_list, start_game, play_again

import unittest


class TestGuessNumber(unittest.TestCase):

    def test_welcome(self):
        expected_message = '¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!'
        self.assertEqual(welcome(), expected_message)         
    
    """ def test_player_name(self, mock_respuesta):
        @mock.patch('mock_example.get_name') 
        pass """
    
    def test_generate_number(self):
        expected_random_number = 60
        generate_number = 60
        self.assertEqual(generate_number(), expected_random_number)

    def test_player_turn(self):
        expected_round = '\n--- Round: {player_name} ---'

    def test_computer_turn(self):
        pass

    def test_guess_number(self):
        pass

    def test_validate_guess(self):
        pass

    def test_tries_list(self):
        pass

    def test_start_game(self):
        expected_flow = welcome(), player

    def test_play_again(self):
        pass

        

if __name__ == '__main__':
    unittest.main()