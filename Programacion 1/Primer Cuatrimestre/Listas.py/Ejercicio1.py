#Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
#Nombre: Lorenzo
#Apellido: Gomez Martins
def calcular_promedio(lista):
    cantidad_elementos = len(lista)
    suma =sum(lista)
    promedio = suma / cantidad_elementos
    return promedio
    

lista = []
cantidad_elementos = int(input("Ingrese una cantidad: "))
for i in range(cantidad_elementos):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)

    
promedio = calcular_promedio(lista)
print(f"El promedio de la suma de los numero es: {promedio}")

######################################

lista = [0] * 5

for i in range(len(lista)):
    lista[i] =int(input("Ingrese un numero: "))
    seguir = input("Desea contuniar? si/no: ")

    if seguir == "si":
        continue
    else:
        break
suma = sum(lista)
promedio = suma / len(lista)
print(promedio)
        
    
 


 
  
  
