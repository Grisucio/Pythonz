#FUNCION: SOLICITAR EDAD, APROBAR O REPROBAR UNA NOTA.

edad = int(input("Dime tu edad: "))

if edad >= 18:
    print("Eres mayor de edad") 
else:
    print("Eres menor de edad")  

nota = float(input("Dime tu nota: "))

     if nota >= 6.0:
                    print("aprobado")
     elif nota >= 5.0:
                      print("bueno")
     elif nota >= 4.0:
                      print("debes mejorar")
     else:
          print("reprobado")


