#FUNCION: VENTA DE COMIDA

print("Bienvenido a la fonda")

precios = {
    "Empanada de pino": 2000,
    "Empanada de queso": 1500,
    "Choripan": 2500,
    "Terremoto": 1000
}

cantidad = {}
total = 0

for producto, precio in precios.items():
    cantidad[producto] = int(input(f"Ingrese la cantidad de {producto}: "))
    total += cantidad[producto] * precio

if total > 20000:
    descuento = 0.40
    mensaje_descuento = "Descuento 40%. Entradas gratis."
elif total > 10000:
    descuento = 0.25
    mensaje_descuento = f"Descuento del 25% aplicado."
else:
    descuento = 0
    mensaje_descuento = "No recibió descuento."

total_con_descuento = total * (1 - descuento)

print(f"Total sin descuento: {total}")
print(f"{mensaje_descuento}")
print(f"Total a pagar: {total_con_descuento}")
