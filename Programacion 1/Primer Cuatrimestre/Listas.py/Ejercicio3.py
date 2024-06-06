#Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
#Nombre: Lorenzo
#Apellido: Gomez Martins

def calcular_producto(lista: list) -> int:
    cantidad_elementos = len(lista)
    
   

lista = []
cantidad_elementos = int(input("Ingrese una cantidad: "))
for i in range(cantidad_elementos):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)
for i in lista:
    numero *= lista[i]
    resultado = numero
     
     

print(f"El producto es: {resultado}")

##############################################################

def pedir_producto (lista: list) -> int:
    numero += 1
    for i in (len(lista)):
     numero *= lista[i]
    return numero

