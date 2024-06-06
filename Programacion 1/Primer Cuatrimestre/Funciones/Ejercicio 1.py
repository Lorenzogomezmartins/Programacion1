#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
#Nombre: Lorenzo
#Apellido: Gomez Martins
def numero_entero():

    numero = input("Ingrese un numero: ")
    numero = int(numero)
    return numero


num = numero_entero()
print(f"El numero ingresado es: {num}")