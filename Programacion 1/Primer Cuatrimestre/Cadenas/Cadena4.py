#4)ar una función que reciba como parámetro una cadena y suprima los caracteres repetidos.

def suprimir_caracteres(cadena):
    axuliar = " "
    for i in range(len(cadena)):
        if cadena[i] == cadena[i-1]:
            axuliar += cadena[i]
    return axuliar

palabra = suprimir_caracteres ("Hhooollaaaaaaaaa")
print(palabra)