#-Realizar una función recursiva que calcule la suma de los primeros números naturales:

#Nombre: Lorenzo
#Apellido: Gomez Martins
def sumar_naturales (numero:int) -> int:
        if numero == 0:
            return 0
        else:
              return numero + sumar_naturales (numero -1)


numero_suma = 4
resultado = sumar_naturales(numero_suma)
print(f"el resultado de la suma es: {resultado}")
            

#2-Realizar una función recursiva que calcule la potencia de un número:

def potencia_numeros (base:int, potencia:int) -> int:
      if potencia == 0:
            return 1
      else: 
            return base * potencia_numeros (base, potencia -1)
potencia = 3
base = 2

resultado = potencia_numeros(base, potencia)
print(F" El resultado de la potencia de un numero es: {resultado}")


# 3-Realizar una función recursiva que la suma de los dígitos de un número:

def suma_digitos(numero:int) -> int:
      if numero < 10:
            return numero
      else:
            return numero % 10 + suma_digitos(numero // 10)
      

digito = 985
resultado = suma_digitos(digito)
print(f"El resultado de la suma de los digitos es: {resultado}")

#4-Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

def fibonacci(numero:int) -> int:
     if numero < 2:
           return numero
     else:
           return fibonacci (numero -1) + fibonacci (numero -2)

numero_ingresado = input("Ingrese un numero")
numero_ingresado = int(numero_ingresado)
for i in range(numero_ingresado + 1):
      print (fibonacci(i))


           

        
