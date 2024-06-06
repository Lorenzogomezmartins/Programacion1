#Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
#Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
#Mostrar la cantidad de números positivos y negativos.
#Mostrar la sumatoria de los números pares.
#Informar el mayor de los números impares.
#Listar todos los números ingresados.
#Listar todos los números pares.
#Listar los números de las posiciones impares.  
#Salir

#Nombre: Lorenzo
#Apellido: Gomez Martins
from os import system
from Especificas import ingreso_numero, cantidad_negativos, cantidad_positivos
from Especificas import mayor_impar, posicion, Suma_pares
from Array_Generales import mostrar_lista, numeros_impares, numeros_pares

def ingreso_numero (minimo, maximo) -> int:
 numeros = int(input("Ingrese los numeros: "))
 if numeros > maximo or numeros < minimo:
   numeros = int(input("Error, ingrese un numero valido: "))
 return numeros

bandera_ingresos = False
lista_de_ingresos = []


bandera_seguir = True
while bandera_seguir:
    opciones = int(input("""1. Ingrese los numeros\n2. Cantidad de positivos y negativos\n3. Sumatoria de pares\n4. Sumatoria de impares\n5.Lista de los numeros ingresados\n6.Lista de numeros pares\n7.Lista de numeros de posiciones impares\n8.Salir\nElija una opcion: """))

    match opciones:
      case 1:
        ingreso_numero (lista = lista_de_ingresos)

        bandera_ingresos = True
        print(lista_de_ingresos)
        
      case 2:
         if bandera_ingresos == True:
           cantidad_negativos (lista_de_ingresos)
           cantidad_positivos (lista_de_ingresos)
      case 3:
        if bandera_ingresos == True:
          Suma_pares (lista_de_ingresos)
        else:
          print("No se han ingresado numeros pares")
      case 4:
        if bandera_ingresos == True:
          mayor_impar = numeros_impares (lista_de_ingresos)
      case 5:
        if bandera_ingresos == True:
          mostrar_lista (lista_de_ingresos)
      case 6:
        if bandera_ingresos == True:
          Suma_pares = numeros_pares(lista_de_ingresos)
      case 7:
        if bandera_ingresos == True:
          posicion (lista_de_ingresos)
      case 8:
        print("Salir")


system("pause")
system("cls")

    