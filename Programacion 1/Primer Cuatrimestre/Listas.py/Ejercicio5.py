#Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
#Nombre: Lorenzo
#Apellido: Gomez Martins

def pedir_maximo(lista: list) -> int:
    numero_max = 0
    posicion = []
    bandera = True
    for i in range(len(lista)):
        if  bandera == True:
            numero_max = lista[i]
            bandera == False
        else:
            if numero_max < lista[i]:
                numero_max == lista[i]
    for pos in range (len(lista)):
        if lista[pos] == numero_max:
            posicion.append(pos)
            return posicion
        
lista_numeros = [10, 20, 33, 5, 6, 77]
resultado = pedir_maximo(lista_numeros)
print(f"El numero mas grande esta en la posicion: {resultado}")


