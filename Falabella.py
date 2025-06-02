#FUNCION: APLICAR DESCUENTOS

def mostrar_nivel(nombre, puntos):
    print(f"Usuario: {nombre}")
    print(f"Puntos: {puntos}")

    if puntos >= 1000:
        print("Nivel: PREMIUM, tienes un descuento del 25%")
    elif puntos >= 500:
        print("Nivel: ORO, tienes un descuento del 10%")
    elif puntos >= 250:
        print("Nivel: STANDAR, los premios que puedes optar son: Audífonos, relojes y más")
    else:
        print("Aún no tienes nivel, ¡Sigue acumulando puntos!")

    print("¡Sigue usando tus puntos en Falabella!")

mostrar_nivel("Marco", 1500)
mostrar_nivel("Jose Luis", 2500)
mostrar_nivel("Sebastian", 300)
