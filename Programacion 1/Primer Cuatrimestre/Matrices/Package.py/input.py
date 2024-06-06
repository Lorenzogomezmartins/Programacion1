from Validar import *

def get_int (mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    pedir_numero = input(mensaje)
    pedir_numero = int(pedir_numero)
    validate = validacion(pedir_numero, minimo, maximo, mensaje_error)
    return validate
