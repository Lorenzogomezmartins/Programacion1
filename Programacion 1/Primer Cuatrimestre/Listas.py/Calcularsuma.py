#calcular la suma de todos los array
#Nombre: Lorenzo
#Apellido: Gomez Martins

def calcular_suma(lista):
    cantidad_elementos = len(lista)
    suma =sum(lista)
    return suma
    

lista = []
cantidad_elementos = int(input("Ingrese una cantidad: "))
for i in range(cantidad_elementos):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)

    
resultado = calcular_suma(lista)
print(f"La suma de los numero es: {resultado}")
