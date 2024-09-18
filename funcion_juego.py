import random

# Función Bienvenida

def welcome():
    print('¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora.')
   # print('Ambos deben adivinar el número correcto. ¡Mucha suerte!')
    

# Función del juego

def guessNumber(anyplayer, numbrechosen):

    # Genera un número aleatorio entre 1 y 100
    numbrechosen = random.randint(1, 100)
    tentativas = []
    anyplayer = None
    intento = None

    while True:

        if anyplayer < numbrechosen:
            print('Demasiado bajo. ¡Inténtalo de nuevo!')
        elif anyplayer > numbrechosen:
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
        guessNumber() 

#al dejar de INDENTAR se termina el bloque de código
#pass no hace nada 