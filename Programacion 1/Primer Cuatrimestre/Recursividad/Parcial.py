#Desarrollar una función que reciba como parametros el precio de un producto y el porcentaje de descuento que se aplicara. La funcion retornara el precio del producto con descuento.  (Enviar aqui link de GDB)


def funcion (precio: int, descuento: int) -> int:

    if precio < 0:
        return precio
    else:
        return precio * 100 / descuento
    
precio = 582
descuento = 5
resultado = funcion(precio, descuento)
print(f"El precio de su producto es de: {precio}, con un descuento de: {descuento}, en total paga: {resultado}")


