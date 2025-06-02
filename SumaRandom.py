#def suma(a, b):
    #return a + b

#print("vamos a hacer una suma: ")

#a = int(input("dime un numero: "))     # ESTA ES UNA SUMA CON NUMEROS
#b = int(input("dime un numero: "))     #QUE LE PREGUNTEMOS A LA PERSONA

#resultado = suma(a, b)
#print("el resultado es: ", resultado)

import random #Aqui importamos una "biblioteca" llamada random
print("")

def suma(a, b):
    return a + b

a = random.randint(1, 10) #Aqui decidimos que variables seran las que
b = random.randint(1, 10) #Utilizaremos para que sean random

print("los numeros escogidos aleatoriamente son: ", a,"y", b)
print("")               # ESTA ES UNA SUMA CON NUMEROS RANDOM 

resultado = suma(a, b)
print("El resultado es: ", resultado,)


