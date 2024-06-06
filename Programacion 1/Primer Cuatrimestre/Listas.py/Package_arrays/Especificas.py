from Array_Generales import numeros_pares , numeros_impares


def ingreso_numero (minimo, maximo) -> int:
 numeros = int(input("Ingrese los numeros: "))
 if numeros > maximo or numeros < minimo:
   numeros = int(input("Error, ingrese un numero valido: "))
 return numeros


def cantidad_positivos (lista: list) -> list:
  
  for i in range(len(lista)):
    if lista[i] > 0:
      cantidad_pares += 1

  mensaje = f"La cantidad de positivos es: {cantidad_pares}"
  print(mensaje)


def cantidad_negativos (lista: list) -> list:
  
  for i in range(len(lista)):
    if lista[i] < 0:
      suma_impares += 1
   
  mensaje = f"La cantidad de impares es: {suma_impares}"
  print(mensaje)

def Suma_pares (lista: list) -> list:
  suma = 0
  numero = numeros_pares (lista = lista)

  for i in range (len(lista)):
    suma = suma + numero[i]

  mensaje = f"La sumatoria de los numeros pares es: {suma}"
  print(mensaje)


def mayor_impar (lista: list) -> list:
  bandera_imar = False
  numero = numeros_impares (lista = lista)

  for i in range(len(lista)):
    if bandera_imar == False or numero[i] > maximo:
      maximo = numero[i]
      bandera_imar = True

def posicion (lista: list) -> list:
  posiciones_imar = []
  for i in range(len(lista)):
    if (lista[i] % 2) == 1:
      posiciones_imar.append[i]
  return posicion