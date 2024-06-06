# 1)Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
# Por ej:
# cadena = “murcielaguito”

#Nombre: Lorenzo
#Apellido: Gomez Martins
def contar_vocales (cadena):
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0



    for letra in cadena:
        match letra:
            case "a":
                contador_a += 1
            case "e":
                contador_e += 1
            case "i":
                contador_i += 1
            case "o":
                contador_o += 1
            case "u":
                contador_u += 1

    matriz = ["a", contador_a,], ["e", contador_e], ["i", contador_i], ["o", contador_o], ["u", contador_u]
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila[0], ":", fila[1])

cadena = "hipopotamo"
resultado = contar_vocales(cadena)
mostrar_matriz(resultado)

