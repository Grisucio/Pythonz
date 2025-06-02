#FUNCION: VENTA DE PRODUCTOS 

pollo = 1000 + 1200 + 500
merma = pollo * 0.25
print(f"Merma total de la semana: {merma} kg")

productos = {
    "leche": 50, "arroz": 60, "pan": 80, "huevos": 100, "aceite": 40,
    "jabon": 30, "queso": 20, "azucar": 70, "harina": 60, "detergente": 35
}

devoluciones_realizadas = 0

while devoluciones_realizadas < 3:
    prod = input("Ingrese el producto a devolver (o 'salir' para terminar): ").lower()
    
    if prod == "salir":
        break
    
    if prod in productos:
        try:
            cant = int(input(f"Cantidad de {prod} a devolver: "))
            
            if cant <= productos[prod] * 0.2:
                print("Devolución aceptada")
                devoluciones_realizadas += 1
            else:
                print("Error: La cantidad supera el 20% permitido")
        except ValueError:
            print("Error: Ingresa un número válido")
    else:
        print("Error: Producto no encontrado")

print("Programa finalizado")
