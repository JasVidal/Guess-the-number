import random

# Genera un número aleatorio entre 1 y 100
random_number = random.randint(1, 100)
player = None

print("¡Bienvenido a Guess the Number! En este juego, eres tú Vs. la computadora.")
print("Ambos deben adivinar el número correcto. ¡Mucha suerte!")

while True:
    # Turno del jugador
    print('\n--- Round: Player ---')
    player = int(input('Escribe tu adivinanza (un número entre 1 y 100): '))
    
    # Verifica la adivinanza del jugador
    if player < random_number:
        print('Demasiado bajo. ¡Intpentalo de nuevo!')
    elif player > random_number:
        print('Demasiado alto. ¡Intpentalo de nuevo!')
    else:
        print('¡Felicidades! Has adivinado el número.')
        break

    # Turno de la computadora
    computer_choice = random.randint(1, 100)
    print(f'La computadora elige: {computer_choice}')

    # Verifica la adivinanza de la computadora
    if computer_choice < random_number:
        print('Demasiado bajo. ¡Intpentalo de nuevo!')
    elif computer_choice > random_number:
        print('Demasiado alto. ¡Intpentalo de nuevo!')
    else:
        print('¡La computadora ha adivinado el número!')
        break
