#Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
#Nombre: Lorenzo
#Apellido: Gomez Martins
def numero_mas_grande():
    numeros = []
    for i in range(3):
        numero = input("Ingrese el numero: ")
        numero = float(numero)
        numeros.append(numero)

    maximo = max(numeros)
    return maximo

maximo = numero_mas_grande()
print(f"El numero maximo es: {maximo}")


