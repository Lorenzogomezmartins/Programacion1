#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
#Nombre: Lorenzo
#Apellido: Gomez Martins
def numero_par_o_Imar():
    numero = input("Ingrese un numero:")
    numero =int(numero)

    if numero %2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


print("Bienvenidos")
numero_par_o_Imar()