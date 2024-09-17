import random

#El jugador ingresa su nombre

player_name = input('¡Hola! ¿Cuál es tu nombre?')

# Genera un número aleatorio entre 1 y 100
random_number = random.randint(1, 100)
tentativas = []
player = None
intento = None

print("¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora.")
print("Ambos deben adivinar el número correcto. ¡Mucha suerte!")

while True:
    # Turno del jugador
    print('\n--- Round:' + player_name + ' ---')
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
        for t in tentativas:
            print(t)
        
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

    


