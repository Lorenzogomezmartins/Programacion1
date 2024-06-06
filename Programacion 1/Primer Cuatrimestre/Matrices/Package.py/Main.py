#Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
#1-Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
#2-Mostrar la recaudación de cada coches y líneas.
#3-Calcular y mostrar recaudación por línea.
#4-Calcular y mostrar recaudación por coche.
#5-Calcular y mostrar la recaudación total.
#6-Salir

#Nombre: Lorenzo
#Apellido: Gomez Martins

from os import system
from Operaciones import *
from Planilla import *
import random




bandera_ingreso = True
planilla = crear()
while bandera_ingreso:
    opcion = int(input("""1-Cargar datos: \n2-Mostrar la recaudación de los coches y lineas: \n3-Calcular la recaudación por linea: /4Mostrar recaudacion por coche: \n5-Calcular la recaudación total: \n6-Salir\nElija una opcion: """))
    match opcion:
            case 1:
                cargar_datos (planilla)
            case 2:
                mostrar_coches_lineas (planilla)
            case 3:
                mostar_recaudacion_por_linea(planilla)
            case 4:
                mostrar_por_coche(planilla)
            case 5:
                recaudacion_total(planilla)
            case 6:
                print("Usted salio")
                break

system("pause")
system("cls")