#3)Crear una función que reciba como parámetro una cadena y determine si la misma es o no un
#palíndromo. Deberá retornar un valor booleano indicando lo sucedido.

def palindromo (cadena):
    retorna = True

    auxiliar = len(cadena)
    for i in range (auxiliar):
        if cadena[i] != cadena[(auxiliar-1)-i]:
            retorna = False
            break
    return retorna

palabra = palindromo("hola")
print(palabra)
