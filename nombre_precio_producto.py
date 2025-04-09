nombre = input("Digite el nombre del producto: ")
precio = int(input("Digite el precio del producto: "))
descuento = int(input("Digite el descuento que le quiere aplicar al producto: "))
descuento_producto = int(precio * descuento) / 100
precio_final = (precio - descuento_producto)
print(f"El producto ya con el descuento equivale a: {descuento_producto}")
print(f"El nombre del producto es {nombre} y el precio final ya con el descuento es: {precio_final}")
