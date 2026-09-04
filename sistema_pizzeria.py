def calcular_descuento(subtotal):
    if subtotal >= 30000:
        descuento = subtotal * 0.10
    else:
        descuento = 0
        
    return descuento


# Pedir cantidad
cantidad = int(input("Cantidad de pizzas: "))

while cantidad <= 0:
    print("La cantidad debe ser mayor que 0.")
    cantidad = int(input("Cantidad de pizzas: "))
