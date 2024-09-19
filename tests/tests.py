from main import welcome, guess_number, player_name, player_turn, computer_turn
import unittest

class TestGuessNumber(unittest.TestCase):

    def test_random_number(self):
        expected_random_number = 60

        def mock_player_turn():
            return expected_random_number
        
        #Usar el número simulado
        #usar patch
        guess_number()

        #Verificar que el número simulado está en el rango
        self.assertIn(expected_random_number, range(1, 101))

if __name__ == '__main__':
    unittest.main()