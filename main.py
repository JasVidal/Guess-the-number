import random

#---- Función: Bienvenida ----

def welcome():
    return print('¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!')
    

#---- Función: Jugador ingresa su nombre ----

def set_player_name():    
    name = input('¡Hola! ¿Cuál es tu nombre?')
    print(f'¡Buenísimo {name}! ¡Que comience el juego!')
    return name


#---- Función: Generar número aleatorio ----

def generate_number():
    return random.randint(1, 100)


#---- Función: Turno Jugador ingresa su respuesta ----

def player_turn(player_name):
    print(f'\n--- Round: {player_name} ---')
    try:
        return int(input('Escribe tu respuesta (un número entre 1 y 100): '))
    except ValueError:
        print('Por favor ingresa un número entero.')
    return None # Devuelve error: cuando no se escribe un número válido
        
#---- Función: Turno Computadora ingresa su respuesta ----

def computer_turn():
    print('\n--- Round: Computer  ---')
    computer_guess = generate_number()
    print(f'La computadora elige:, {computer_guess}')
    return computer_guess

#---- Bucle del juego ----

def guess_number(player_name):
    #Se trae función Generar número aleatorio
    number_to_guess = generate_number()

    turn = "Player"
    player_tries = []
    computer_tries = []

    while True:
       
        if turn == "Player":
            player_guess = player_turn(player_name)
            # Agrega el intento a la lista
            player_tries.append(player_guess)

        else:
            player_guess = computer_turn()
            # Agrega el intento a la lista
            computer_tries.append(player_guess)
            
        if player_guess is None:
            continue #Vuelve a intentar
        
        result = validate_guess(player_guess, number_to_guess)

        print(result)

        # Mensaje de fin del juego
        if result == '¡Felicidades! Has adivinado el número.':
            tries_list(turn, player_tries, computer_tries)
            return turn

        if turn == 'Player':
            turn = 'Computer'

        else:
            turn = 'Player'

#---- Función Comparación ----

def validate_guess(player_guess, number_to_guess):

    if player_guess < number_to_guess:
        result = ('Demasiado bajo. ¡Inténtalo de nuevo!')
    elif player_guess > number_to_guess:
        result = ('Demasiado alto. ¡Inténtalo de nuevo!')
    else:
        result = ('¡Felicidades! Has adivinado el número.')
    return result
    

#---- Genera una lista para intentos ----

def tries_list(winner, player_tries, computer_tries):
    if winner == "Player":
        print(f'¡Ganaste en {len(player_tries)} intentos!')
        #Mostrar lista de intentos realizadas
        print('Tus intentos fueron:')
        for try_number in player_tries:
            print(try_number)

    else:
        print(f'¡La computadora ganó en {len(computer_tries)} intentos!')
        print('Los intentos de la computadora fueron:')
        for try_number in computer_tries:
            print(try_number)

#---- Empieza el juego ----

def start_game():
    welcome()
    #Turno del jugador
    player_name = set_player_name()

    #Turno del computadora
    guess_number(player_name)
    play_again()
    

#---- Función Volver a jugar ----

def play_again():
    restart_game = input ('\n ¿Deseas jugar otra vez? Responde: Sí/No - ')

    if restart_game.lower() == 'sí' or restart_game.lower() == 'si':
        print('¡Genial! ¡Volvamos a jugar!\n')
        start_game()

    else: 
        print('Gracias por jugar. ¡Hasta la próxima!')

    
if __name__ == '__main__':
    start_game()