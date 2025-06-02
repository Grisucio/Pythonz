#FUNCION: REGISTRAR PACIENTES

def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Ingresa un número válido.")

def registrar_pacientes():
    pacientes = []
    num_personas = validar_entero("¿Cuántas personas vas a registrar?: ")

    for _ in range(num_personas):
        print("\nRegistro de paciente:")
        nombre = input("Nombre: ")
        rut = input("RUT: ")
        enfermedad = input("¿Tienes alguna enfermedad?: ")
        alergia = input("¿Tienes alguna alergia?: ")

        if not nombre or not rut:
            print("Esquema incompleto. Por favor, ingresa toda la información.")
            continue

        pacientes.append({"Nombre": nombre, "RUT": rut, "Enfermedad": enfermedad, "Alergia": alergia})

    return pacientes

def mostrar_menu():
    numeros_ingresados = []

    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar un número entre 0 y 100")
        print("2. Mostrar el número mayor")
        print("3. Mostrar el promedio")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            numero = validar_entero("Ingresa un número entre 0 y 100: ")
            if 0 <= numero <= 100:
                numeros_ingresados.append(numero)
            else:
                print("Número fuera de rango.")

        elif opcion == "2":
            if numeros_ingresados:
                print("Número mayor ingresado:", max(numeros_ingresados))
            else:
                print("No se ha ingresado ningún número.")

        elif opcion == "3":
            if numeros_ingresados:
                print("Promedio de números ingresados:", sum(numeros_ingresados) / len(numeros_ingresados))
            else:
                print("No se ha ingresado ningún número.")

        elif opcion == "4":
            print("Fin del programa.")
            break

        else:
            print("Opción inválida. Inténtalo nuevamente.")

print("Bienvenido")
pacientes_registrados = registrar_pacientes()
mostrar_menu()
