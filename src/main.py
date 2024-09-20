import random


#---- Función: Bienvenida ----

def welcome():
    return print('¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!')
    

#---- Función: Jugador ingresa su nombre ----

def set_player_name():    
    name = input('¡Hola! ¿Cuál es tu nombre?')
    return name


#---- Función: Generar número aleatorio ----

def generate_number():
    random_number = random.randint(1, 100)
    return random_number


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

    while True:
       
        if turn == "Player":
            player_guess = player_turn(player_name)

        else:
            player_guess = computer_turn()
            
        if player_guess is None:
            continue #Vuelve a intentar
        
        new_message = validate_guess(player_guess, number_to_guess)

        print(new_message)
        # Mensaje de fin del juego

        if new_message == '¡Felicidades! Has adivinado el número.':
            print('\n --- Fin del juego ---')
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

def tries_list():
    try_list = []
    try_number = None
    print(f'¡Ganaste en {len(try_list)} intentos!')


    # Agrega el intento a la lista
    try_list.append(try_number)
    
    #Mostrar lista de intentos realizadas
    print('Tus intentos fueron:')
    for try_number in try_list:
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
    restart_game = input ('\n ¿Deseas jugar otra vez? Responde: Sí/No')

    if restart_game.lower() == 'sí' or restart_game.lower() == 'si':
        print('¡Genial! ¡Volvamos a jugar!')
        start_game()

    else: 
        print('Gracias por jugar. ¡Hasta la próxima!')

    #-------------------------------------------
""" while True:
        # Turno del jugador
        print(f'\n--- Round: {set_player_name}  ---')
        player_choice = int(input('Escribe tu respuesta (un número entre 1 y 100): '))
        
        #Añadir el intento a la lista de tentativas
        tentativas.append(player_choice)

        # Verifica la adivinanza del jugador

        if player_choice < random_number:
            print('Demasiado bajo. ¡Inténtalo de nuevo!')
        elif player_choice > random_number:
            print('Demasiado alto. ¡Inténtalo de nuevo!')
        else:
            print('¡Felicidades! Has adivinado el número.')
            
            #Mensaje de fin del juego
            print('\n --- Fin del juego ---')
            print(f'¡Ganaste en {len(tentativas)} intentos!')

            #Mostrar intentos (tentativas) realizadas
            print('Tus intentos fueron:')
            for intento in tentativas:
                print(intento)
            
            break

        # Turno de la computadora
        print('\n--- Round: Computer ---')

        #La computadora hace una elección basándose en la respuesta del jugador
        if player_choice < random_number:
            #La respuesta del jugador es bajo, la computadora adivina un número mayor
            computer_choice = random.randint( player_choice + 1, 100)
        elif player_choice > random_number:
            #La respuesta del jugador es alto, la computadora adivina un número menor
            computer_choice = random.randint(1, player_choice - 1)

        computer_choice = random.randint(1, 100)
        print(f'La computadora elige:', computer_choice)

        # Verifica la adivinanza de la computadora
        if computer_choice < random_number:
            print('Demasiado bajo. ¡Inténtalo de nuevo!')
        elif computer_choice > random_number:
            print('Demasiado alto. ¡Inténtalo de nuevo!')
        else:
            print('¡La computadora ha adivinado el número!')
            break
    """

if __name__ == '__main__':
    start_game()



