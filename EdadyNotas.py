#FUNCION: SOLICITAR EDAD, APROBAR O REPROBAR UNA NOTA.

edad = int(input("Dime tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")  # Si es mayor de edad
else:
    print("Eres menor de edad")  # Si es menor de edad

nota = float(input("Dime tu nota: "))

     if nota >= 6.0:
                    print("aprobado")
     elif nota >= 5.0:
                      print("bueno")
     elif nota >= 4.0:
                      print("debes mejorar")
     else:
          print("reprobado")


#EDAD
#1.SOLICITAR EDAD.
   #la primera linea de codigo simplemente le pide al usuario su edad. Agregando el int para habilitar al usuario el uso de numeros.

#2.CONDICIONES.
   #La segunda parte del codigo nos introduce a las condiciones, que en este caso la primera seria: si la edad es mayor o igual a 18 se le muestra al usuario que es mayor de edad.
   #y la segunda: si no, mostrar al usuario que es menor de edad.

#NOTAS
#1.SOLICITAR NOTA:
   #La primera parte del codigo nos pide que el usuario indique su nota, usamos el float ademas del input para que se puedan poner decimales al numero,se indican con un . no con una ,

#2.CONDIOCIONES:
   #La segunda parte del codigo es aplicar las condiciones solicitadas segun correspondan con if, elif y else.




