def numeros_pares (lista: list) -> list:
    pares = []

    for i in range(len(lista)):
        if (lista[i] % 2) == 0:
            pares.append (lista[i])
    return pares

def numeros_impares (lista: list) -> list:
    impares = []

    for i in range(len(lista)):
        if (lista[i] % 2) != 0:
            impares.append (lista[i])

    return impares

def mostrar_lista (lista: list) -> list:

    for i in range (len(lista)):
        print(lista[i])

   