#Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
#Nombre: Lorenzo
#Apellido: Gomez Martins

def calcular_promedio(lista):
    cantidad_elementos = 0
    numero = 0
    for i in range(len(lista)):
     if lista[i] > 0:
       numero += lista[i]
       cantidad_elementos += 1
     else:
       continue
    return numero / cantidad_elementos


lista = []
cantidad_elementos = int(input("Ingrese la longitud de su lista: "))
for i in range(cantidad_elementos):
  lista.append(int(input("Ingrese un numero: ")))
print(calcular_promedio(lista))


