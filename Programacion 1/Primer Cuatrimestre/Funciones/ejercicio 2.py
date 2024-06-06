#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
#Nombre: Lorenzo
#Apellido: Gomez Martins

def numero_flotante():
    numero = input("Ingrese un numero: ")
    numero = float(numero)
    return numero


num = numero_flotante()
print(f"El numero ingresado es: {num}")