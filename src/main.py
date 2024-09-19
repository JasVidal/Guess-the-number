import random

# Función Bienvenida

def welcome():
#guardar en variable
    print('¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!')


# Genera un número aleatorio entre 1 y 100
def generate_number():
    random_number = random.randint(1, 100)
    return random_number

# Bucle del juego

def guess_number(human_name):

    number_to_guess = generate_number()
    print(number_to_guess)
    turn = "Player"

    while True:
        #Obtiene número del jugador o cumputadora
        if turn == "Player":
            number = player_turn(human_name)

        else:
            number = computer_turn()
            
        if number is None:
            continue #Vuelve a intentar
        
        new_message = validate_guess(number, number_to_guess)

        print(new_message)
        #Mensaje de fin del juego

        if new_message == '¡Felicidades! Has adivinado el número.':
            print('\n --- Fin del juego ---')
            return turn


        if turn == 'Player':
            turn = 'Computer'

        else:
            turn = 'Player'

#Función validate guess
def validate_guess(number, number_to_guess):
    
    if number < number_to_guess:
        message = ('Demasiado bajo. ¡Inténtalo de nuevo!')
    elif number > number_to_guess:
        message = ('Demasiado alto. ¡Inténtalo de nuevo!')
    else:
        message = ('¡Felicidades! Has adivinado el número.')

    return message

    

# Genera una lista para intentos

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

# Jugador ingresa su nombre
def player_name():    
    name = input('¡Hola! ¿Cuál es tu nombre?')
    return name

# Jugador ingresa su respuesta
def player_turn(human_name):
        
    # Turno del jugador
        print(f'\n--- Round: {human_name} ---')
        try:
            return int(input('Escribe tu respuesta (un número entre 1 y 100): '))
        except ValueError:
            print('Por favor ingresa un número entero.')
        return None #Si no se escribe un número válido
        

# Computador ingresa su respuesta
def computer_turn():
    print('\n--- Round: Computer  ---')
    computer_choice = generate_number()
    print(f'La computadora elige:, {computer_choice}')
    return computer_choice

# Empieza el juego
def start_game():
    welcome()
    human_name = player_name()


    # Turno de computadora
    guess_number(human_name, )

    #-------------------------------------------
""" while True:
        # Turno del jugador
        print(f'\n--- Round: {player_name}  ---')
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



