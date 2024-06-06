#2)Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.

#Nombre: Lorenzo
#Apellido: Gomez Martins

def indice (cadena, caracter):
    retorno = -1
    for i in range (len(cadena)):
        if cadena[i] == caracter:
            retorna = f"El caracter se encuentra en el indice: {i}"
            break
    return retorno

caracter_encontrado = indice("Elefante", "f")
print(caracter_encontrado)
