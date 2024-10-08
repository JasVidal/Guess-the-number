import random


#---- Función: Bienvenida ----

def welcome():
    welcome_message = '¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!'
    print(welcome_message)
    return welcome_message
    

#---- Función: Jugador ingresa su nombre ----

def set_player_name(): 

    while True:   
        name = input('¡Hola! ¿Cuál es tu nombre? ')

        if validate_player_name(name):
            print(f'¡Buenísimo {name}! ¡Que comience el juego!')
            return name
    

#---- Función: Validar nombre ----

def validate_player_name(name):
    #Verificar que se ingrese el nombre y no se quede vacío
    if not name:
        print('Por favor ingresa tu nombre.')
        return False

    if not name.isalpha():
       print('Recuerda que tu nombre solo debe contener letras.')
       return False 
    
    return True

#---- Función: Generar número aleatorio ----

def generate_number():
    return random.randint(1, 100)


#---- Función: Turno Jugador ingresa su respuesta ----

def player_turn(player_name):
    print(f'\n--- Round: {player_name} ---')
    
    player_choice = input('Escribe tu respuesta (un número entre 1 y 100): ')
    return validate_player_choice(player_choice)


#---- Función: Validar Turno Jugador ----

def validate_player_choice(player_choice):
    try:
        player_choice = int(player_choice)
        if 1 <= player_choice <= 100:
            return player_choice
        else:
            print('Debes ingresar un número que sea entre 1 y 100.')
            return None #Devuelve error: si no se escribe dentro del rango
    except ValueError:
        print('Respuesta inválida. Recuerda que debe ser un número entero.')
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
            if player_guess is not None: #Validar que jugador ingresó su respuesta
                player_tries.append(player_guess)
            else:
                continue #Vuelve a intentar


        else:
            player_guess = computer_turn()
            # Agrega el intento a la lista
            computer_tries.append(player_guess)
            
        
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

    player_name = set_player_name()

    guess_number(player_name)

    return play_again()
    

#---- Función Volver a jugar ----

def play_again(): 
    
    restart_game = input ('\n ¿Deseas jugar otra vez? Responde: Sí/No - ')

    if restart_game.lower() in ['sí', 'si']:
        print('¡Genial! ¡Volvamos a jugar!\n')
        return start_game()

    elif restart_game.lower() == 'no':
        print('Gracias por jugar. ¡Hasta la próxima!')
    else:
        print('Error: Tu respuesta es inválida, gracias por jugar. ¡Vuelve pronto!')

    
if __name__ == '__main__':
    start_game()