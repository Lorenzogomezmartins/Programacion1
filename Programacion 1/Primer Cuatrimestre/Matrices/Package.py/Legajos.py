import random

def armar_legajos ( ) :
    legajos = [[0] * 5 for _ in range(3)]

    for i in range (len(legajos)):
        for j in range (len(legajos[i])):
           legajos[i][j] = random.randint(1000, 9999)

    for i in range (len(legajos)):
        for j in range (len(legajos[i])):
            print(f"{legajos[i][j]}", end = " ")
        print("")       

    return legajos

def mostrar_legajos(legajos: list):
    print("Los legajos de los choferes son:")
    for i in range(len(legajos)):        
        mostrar = legajos[i]
        print(f"{mostrar : 05}", end=" ")
        print()


def comprabar (legajos: list):
    bandera = True
    mostrar_legajos = (legajos)
    bandera = True
    while bandera:
        ingreso = int(input("Ingrese su legajo: "))
        for sublist in legajos:
            if ingreso in sublist:
                bandera = False
                print("Legajo correcto")
                break
        if bandera:
            print("Error, el legajo ingresado no es correcto, ingrese nuevamente un legajo correcto: ")
    return bandera
