#A) Los datos a ingresar por cada empleado encuestado son:
#nombre del empleado
#edad (no menor a 18)
#género (Masculino - Femenino - Otro)
#tecnologia (IA, RV/RA, IOT)  
#B) Cargar por terminal 10 encuestas.
#C) Determinar:
#Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
#Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
#Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

#Nombre: Lorenzo
#Apellido: Gomez Martins

g_masculino_votaron_IA_IOT = 0
no_votaron_IA= 0
g_femenino = 0
g_masculino = 0
g_otro = 0
edad_m = 0
edad_f = 0
edad_otro = 0
mayor_edad = 0
tec_mayor_edad = ""
nombre_mayor = ""
contador = 0
for cantidad in range (0,11):


    Nombre = input("Ingrese su nombre:")
    edad = int(input("Ingrese su edad:"))
    while edad < 18:
     edad = input("Ingese su edad porfavor:")
    Genero = input("Ingrese su genero:")
    while Genero != "Masculino" and Genero != "Femenino" and Genero != "Otro":
      Genero = input("Ingrese su genero porfavor:")
    Tecnologia = input("Ingrese la tecnologia:")
    while Tecnologia != "IA" and Tecnologia != "RV/RA" and Tecnologia != "IOT":
         Tecnologia = input("Ingrese la tecnologia porfavor:")


#Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
if Genero == "Masculino" and (Tecnologia == "IOT" or Tecnologia == "IA") and (edad >= 25 and edad <= 50):
   g_masculino_votaron_IA_IOT += 1

#Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
if Genero != "Femenino" and (Tecnologia != "IA") and (edad >= 33 and edad <= 40):
   no_votaron_IA += 1

#Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
if Genero == "Masculino":
   g_masculino += 1
   edad_m += edad
elif Genero == "Femenino":
   g_femenino += 1
   edad_f += edad
elif Genero == "Otro":
   g_otro += 1
   edad_otro += edad

if Genero == "Masculino" and edad > edad_m:
   mayor_edad = edad
   tec_mayor_edad = Tecnologia
   nombre_mayor = Nombre

contador += 1

porcentaje = (no_votaron_IA / contador) * 100

Mensaje_1 = f"la cantidad de empleados que votaron por IOT e IA y son de sexo Masculino es de: {g_masculino_votaron_IA_IOT}"
Mensaje_2 = f"El porcentaje de personas que no votaron por IA es de: {porcentaje}%"
Mensaje_3 = f"el nombre de la persona de genero masculino de mayor edad es {0} y su tecnologia es {1}".format(nombre_mayor,tec_mayor_edad)

print(Mensaje_1)
print(Mensaje_2)
print(Mensaje_3)

