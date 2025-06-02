#FUNCION: AREA DE UN TRIANGULO

try:
    cantidad = int(input("Cantidad de triángulos: "))

    while cantidad > 0:
        try:
            base = float(input("Base: "))
            altura = float(input("Altura: "))

            if base > 0 and altura > 0:
                print(f"Área: {base * altura / 2}")
                cantidad -= 1
            else:
                print("Los valores deben ser positivos.")
        except ValueError:
            print("Entrada inválida, usa números.")
except ValueError:
    print("Entrada inválida, usa un número entero.")
