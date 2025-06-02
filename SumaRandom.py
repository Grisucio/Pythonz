#FUNCION: SUMA IMPORTANDO BIBLIOTECA RANDOM.

import random

def suma(a, b):
    return a + b

a = random.randint(1, 10)
b = random.randint(1, 10)

print(f"Los números escogidos aleatoriamente son: {a} y {b}\n")
print(f"El resultado es: {suma(a, b)}")


