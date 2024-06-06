#Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
#Nombre: Lorenzo
#Apellido: Gomez Martins

#PUNTO 1
def entero ():
 while True:
  try:
   numero = int(input("Ingese un numero entero: "))
   return numero
  except ValueError:
   print("Ingrese un numero entero valido")
    

num_entero = entero()
print(f"El numero entero ingresado es: {num_entero}")


#PUNTO 2

def flotante():
 while True:
  try:
   numero = float(input("Ingrese un numero con decimal "))
   return numero
  except ValueError:
   print("El numero es incorrecto")


num_flotante = flotante()
print(f"El numero flotante ingresado es: {num_flotante}")


#PUNTO 3

def ingresar_cadena():
 while True:
   cadena = input("Ingrese una cadena")
   if cadena.strip():
    return cadena
   else: 
    print("Introduzca una cadena valida")

cadena_2 = ingresar_cadena()
print(f"La cadena ingresada es: {cadena_2}")
  

     

    
