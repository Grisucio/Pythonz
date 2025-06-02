#FUNCION: CALCULAR SUBCIDIO DE GAS

quintil = int(input("Ingresa tu quintil: "))
condicion = input("Ingresa tu condición laboral (empleado/desempleado): ").lower()
edad = int(input("Dime tu edad: "))

subsidio = 0
bono = 0

if quintil == 1:
    subsidio = 15000 if condicion == "desempleado" else 10000
elif quintil == 2:
    subsidio = 15000 if condicion == "desempleado" else 10000
elif quintil == 3:
    subsidio = 8000 if condicion == "desempleado" else 6000
elif quintil == 4:
    subsidio = 6000 if condicion == "empleado" else 0
elif quintil == 5:
    subsidio = 1500

if quintil in (1, 2):
    bono += 2000

if edad > 65:
    bono += 3000

total = subsidio + bono

print(f"El subsidio total que te corresponde es: ${total}")




