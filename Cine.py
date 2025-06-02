#FUNCION: VENTA DE ENTRADAS AL CINE.
def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Ingresa un número válido.")

entradas = 100

print("Bienvenido al sistema de venta de entradas del cine")

while True:
    print("\nMenú de opciones:")
    print("1. Ver entradas disponibles")
    print("2. Comprar entradas")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Entradas disponibles: {entradas}")

    elif opcion == "2":
        cantidad = validar_entero("Cantidad a comprar: ")
        
        if cantidad > entradas:
            print("No hay suficientes entradas disponibles.")
        elif cantidad <= 0:
            print("Debes ingresar un número positivo.")
        else:
            entradas -= cantidad
            print(f"Compra realizada. Quedan {entradas} entradas.")

    elif opcion == "3":
        print("¡Gracias por tu visita! Hasta la próxima.")
        break

    else:
        print("Opción no válida. Inténtalo nuevamente.")

