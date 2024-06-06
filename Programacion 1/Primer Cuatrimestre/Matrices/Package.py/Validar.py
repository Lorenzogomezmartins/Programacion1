def validacion (pedir_numero: int|float, minimo: int, maximo: int, mensaje_error: int):

    while pedir_numero < minimo or pedir_numero > maximo:
        pedir_numero = (mensaje_error)
        pedir_numero = int(pedir_numero)
    return pedir_numero
    
    