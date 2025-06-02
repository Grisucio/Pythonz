"""
# while
contador = 1
while contador <=3:
    print("Hola", contador)

contador += 1

edad = 10
if edad <= 18:
    print("eres mayor de edad")
else: 
    print("eres menor de edad")


1- El programa deberia comenzar permitiendo ingresar un numero de personas que va a registrar, debe ser numero entero.
luego se debe registrar cada paciente con sus datos (nombre, rut), debe solcitiar info (enfermedad, alergias)
en caso de que no responda una pregunta debe decir Esquema incompleto, una vez ingresada toda la info
el programa debe mostrar la informacion obtenida, Cada ingreso debe manejarse con una excepcion(informacion erronea)
debe preguntar hasta que se cumpla la entrega de la informacion completa, por ultimo solicitar un numero para salir
y mensaje de despedida.

2- Realice un menu que pueda hacer una funcionalidad, mostramos menu principal y añadimos las opciones

1.Ingresa un numero: Debe permitir ingresar un numero entero entre el 0 y el 100. El usuario puede ingresar cualquier valor dentro del rango por lo que debemos manejar
excepciones, incluso puede ingresar string
2.Mostrar el mayor: Debe mostrar el numero mayor ingresado hasta ese momento
3.Mostrar el promedio: Debe mostrar el promedio ingresado hasya ese momento, para ambas opciones, si no se a ingresado ningun numero debe indicar no se ha ingresado ningun intento
4.Para salir: el mensaje seria "fin del programa"
"""
print("Bienvenido")
NumeroPersonas = input(int("¿Cuantas personas registraras?: "))
NombrePaciente = input("Dime tu nombre: ")
RutPaciente = input("Ingresa tu rut: ")
EnfAdic = input("¿Tienes alguna enfermedad?: ")
AlerAdic = input("¿Tienes alguna alergia a algun medicamento?: ")

print("")