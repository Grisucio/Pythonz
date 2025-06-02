VERIFICAR NUMERO POSITIVO O NEGATIVO.

variable1 = int(input("ingresa un numero: "))

if variable1 < 0:    
    print("tu numero es negativo")
elif variable1 > 0:   
    print("tu numero es positivo")
else:   
    print("tu numero es igual cero") 



#1.Se le pide al usuario ingresar el entero y se almacena en "variable1"

#2.Ahora se crea una condicion con un if (que es "si" al españoluwu) si la "variable1" es menor (<) a 0. Osea diria: "si el dato ingresado es menor a 0:",  y si ese es el caso pasaria a mandar un mensaje "tu numero es negativo" ya que el numero seria inferior a 0.

#3.Se agrega una segunda condicion con elif,que es "else if"(en español seria como "ademas"uwu). Elif es por si no se cumple la primera condicion, asi pasa a la segunda que seria esta. Que es muy parecida solo que ahora verifica si "variable1" es positiva, osea si es mayor(>) a 0 y pasa a mandar el mensaje "tu numero es positivo".

#4.Se agrega una tercera condicion que es por si ninguna de las anteriores se cumple. con "else"(que al español es como si nouwu) y solo se manda el mensaje "tu numero es igual a 0".