
import random

# La computadora adivina el número

def computerChoice():
    print('\n--- Round: Computer ---')
    
    while True:
        random_number = random.randint(1, 100)

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