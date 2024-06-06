#Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:
#Nombre: Lorenzo
#Apellido: Gomez Martins
def get_int (mensaje: str, mensaje_erroneo: str, minimo: int, maximo: int, reitentos: int) -> int|None:
 
 nota= input(mensaje)
 nota = int(nota)
 contador_intentos = 0

 while nota < minimo or nota > maximo:
  nota = input(f"{mensaje_erroneo}")
  nota = int(nota)
  contador_intentos += 1
  if contador_intentos == reitentos:
   return None
   break
 return nota
   

 
  
print_1 = get_int("Bienvenidos, ingrese su nota: ", "Error, ingrese una nota correcta: ", 1, 10, 3)

#Repetir el mismo procedimiento para un dato de tipo float.
def get_float (mensaje: str, mensaje_erroneo: str, minimo: float, maximo: float, reitentos: float) -> float|None:
 
 edad = input(mensaje)
 edad = float(edad)
 contador_intentos = 0

 while edad < minimo or edad > maximo:
  edad = input(f"{mensaje_erroneo}")
  edad = float(edad)
  contador_intentos += 1
  if contador_intentos == reitentos:
   return None
   break
 return edad
   

 
  
print_2 = get_float("Bienvenidos, ingrese su edad: ", "Error, ingrese una edad correcta: ", 1, 100, 3)

#2-Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):

def get_string(mensaje: str, mensaje_erroneo: str, longitud: int, reitentos: float) -> str|None:

    nombre_ingresado = input(mensaje)
    longitud_de_la_palabra = len(nombre_ingresado)
    contador = 0
    
    while longitud_de_la_palabra > longitud:
     nombre_ingresado = input(mensaje_erroneo)
     longitud_de_la_palabra = len(nombre_ingresado)
     contador += 1
     return None
     break
    return nombre_ingresado

nombre = get_string("Ingrese su nombre: ", "Error, ingrese su nombre:", 12, 3)
print(f"Su nombre es: {nombre}")

#3-

