import random

# Función Bienvenida

def welcome():
#guardar en variable
    print('¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora. \n Ambos deben adivinar el número correcto. ¡Mucha suerte!')


# Genera un número aleatorio entre 1 y 100
def number_generated():
    random.randint(1, 100)
    return number_generated

# Bucle del juego

def guess_number():

    

    turn = "Player"
    # Genera una lista para intentos
    tryList = []
    tryNumber = None

    while True:
        #Obtiene número del jugador o cumputadora
        if turn == "Player":
            number = player_turn()

        else:
            number = computer_turn()
            
        if number is None:
            continue #Vuelve a intentar

        # Agrega el intento a la lista
        tryList.append(number)

        if number < number_generated:
            print('Demasiado bajo. ¡Inténtalo de nuevo!')
        elif number > number_generated:
            print('Demasiado alto. ¡Inténtalo de nuevo!')
        else:
            print('¡Felicidades! Has adivinado el número.')

            #Mensaje de fin del juego
            print('\n --- Fin del juego ---')
            print(f'¡Ganaste en {len(tryList)} intentos!')

            #Mostrar lista de intentos realizadas
            print('Tus intentos fueron:')
            for tryNumber in tryList:
                print(tryNumber)
            break

        if turn == 'Player':
            turn = 'Computer'

        else:
            turn = 'Player'

# Jugador ingresa su nombre
def player_name():    
    name = input('¡Hola! ¿Cuál es tu nombre?')
    return name

# Jugador ingresa su respuesta
def player_turn():
        
    # Turno del jugador
        print('\n--- Round: Jugador ---')
        try:
            return int(input('Escribe tu respuesta (un número entre 1 y 100): '))
        except ValueError:
            print('Por favor ingresa un número entero.')
        return None #Si no se escribe un número válido
        

# Computador ingresa su respuesta
def computer_turn():
    print('\n--- Round: Computer  ---')
    computer_choice = random.randint(1, 100)
    print(f'La computadora elige:, {computer_choice}')
    return computer_choice

# Empieza el juego
def start_game():
    welcome()
    name = player_name()

    # Turno de computadora
    guess_number()

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



