#FUNCION: JUEGO ADIVINANZA

import random

inicio = int(input("Ingresa el número menor del rango: "))
fin = int(input("Ingresa el número mayor del rango: "))

if inicio >= fin:
    print("El primer número debe ser menor que el segundo.")
else:
    numero = random.randint(inicio, fin)
    numero = round(numero / 4) * 4  

    for intento in range(1, 4):
        adivina = int(input("Adivina el número: "))

        if adivina == numero:
            if intento == 1:
                print("¡Felicitaciones, adivinaste en el primer intento!")
            else:
                print("¡Bien hecho, adivinaste!")
            print("Fin del juego.")
            break
        elif adivina < numero:
            print("Pista: el número es mayor.")
        else:
            print("Pista: el número es menor.")

    else:
        print("Perdiste, el número era", numero)
