from main import welcome, set_player_name, generate_number, player_turn, computer_turn, guess_number, validate_guess, tries_list, start_game, play_again
from unittest.mock import patch, Mock
import unittest

mock = Mock()
class TestGuessNumber(unittest.TestCase):

    #Test Función Welcome / No se necesita
    def test_welcome(self):
        expected_message = '¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!'
        self.assertEqual(welcome(), expected_message)         
    
    #Test Función Set Player Name / No se necesita
    @patch('main.set_player_name', return_value = "Pepito")
    def test_set_player_name(self, mock_player_name): 
       # mock_player_name.return_value = "Pepito"
        self.assertEqual(mock_player_name(), "Pepito")
    

    #Test Generate Number / No se necesita
    def test_generate_number(self):
        expected_random_number = 60
        generate_number = 60
        self.assertEqual(generate_number, expected_random_number)


    #Test Player Turn / No se necesita
    def test_player_turn(self):
        pass
    

    #Test Computer Turn / No se necesita
    def test_computer_turn(self):
        pass
    

    #Test Guess Number Player Winner
    @patch('main.generate_number', return_value = 20)
    @patch('main.player_turn', return_value = 20)
    def test_player_winner(self, mock_generate_number, mock_player_turn):
        result_guess = guess_number(player_name='Jas') 
        self.assertEqual(result_guess, 'Player')


     #Test Guess Number Computer Winner
    @patch('main.player_turn', return_value = 5)
    @patch('main.computer_turn', return_value = 30)
    @patch('main.generate_number', return_value = 30)
    def test_computer_winner(self, mock_player_turn, mock_computer_turn, mock_generate_number):
        result_guess = guess_number(player_name='Jas')
        self.assertEqual(result_guess, 'Computer')

    #Test Validate Guess
    def test_validate_guess_lower(self):
        result_lower = validate_guess(player_guess=10, number_to_guess=20)
        self.assertEqual(result_lower, 'Demasiado bajo. ¡Inténtalo de nuevo!')

    def test_validate_guess_higer(self):
        result_higer = validate_guess(player_guess=20, number_to_guess=10)
        self.assertEqual(result_higer, 'Demasiado alto. ¡Inténtalo de nuevo!')

    def test_validate_guess_equal(self):
        result_equal = validate_guess(player_guess=20, number_to_guess=20)
        self.assertEqual(result_equal, '¡Felicidades! Has adivinado el número.')

    
    #Test Tries List
    def test_tries_list(self):
        pass
    

    #Test StarGame2 
    @patch('main.welcome', return_value = '¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!')
    @patch('main.set_player_name', return_value = 'Jas')
    @patch('main.guess_number', return_value = None)
    @patch('main.play_again', return_value = 'si')
    def test_start_game(self, mock_welcome, mock_set_player_name, mock_guess_number, mock_play_again):
        result = start_game()

        #Verificar que se llama al mock
        mock_play_again.assert_called()

        #Resultado
        self.assertEqual(result, 'si')

    #Test Play Again
    @patch('main.play_again', return_value = 'Si')
    def test_play_again(self, mock_play_again):
        self.assertEqual(mock_play_again(), 'Si')

        

if __name__ == '__main__':
    unittest.main()