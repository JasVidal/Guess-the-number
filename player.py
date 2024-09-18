# El jugador ingresa su nombre
import random

def playerName():    
    return input('¡Hola! ¿Cuál es tu nombre?')

# El jugador adivina el número

def playerChoice():
    print('Escribe tu respuesta (un número entre 1 y 100): ')

while True:

    # Genera un número aleatorio entre 1 y 100
    numbrechosen = random.randint(1, 100)
    tentativas = []
    anyplayer = None
    intento = None

# Turno del jugador
    print(f'\n--- Round: {playerName()}  ---')
    player_choice = int(input('Escribe tu respuesta (un número entre 1 y 100): '))

    #Añadir el intento a la lista de tentativas
    tentativas.append(player_choice)

    # Verifica la adivinanza del jugador

    if player_choice < numbrechosen:
        print('Demasiado bajo. ¡Inténtalo de nuevo!')
    elif player_choice > numbrechosen:
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