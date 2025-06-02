#FUNCION: CALCULAR DESCUENTO MATRICULA.

nota = float(input("Ingresa tu nota: "))

if nota > 6:
    print("¡Felicidades! Tienes un 20% de descuento en tu matrícula.")
elif nota > 5:
    print("¡Muy bien! Tienes un 15% de descuento en tu matrícula.")
elif nota > 4:
    print("¡Bien hecho! Tienes un 10% de descuento en tu matrícula.")
else:
    print("Sigue esforzándote, ¡tú puedes mejorar!")
