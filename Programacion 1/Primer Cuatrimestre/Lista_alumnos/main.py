#Nombre: Lorenzo
#Apellido: Gomez Martins

from os import system
from Validate import *
from Operaciones import *

def elegir_opcion():
    opcion = input("""MENU\n1-Ingrese empleado: \n2-Modificar empleado: \n3-Eliminar Empleado: \n4-Mostrar todos: \n5-Calcular salario promedio:  \n6-Buscar Empleado por DNI: \n7-Ordenar Empleados: \n8-Reporte: \n9-Elija un apellido del usuario: \n10-Salir\nElija una opcion: """)
    return opcion

lista_empleados = []
leer_empleados(lista_empleados)
numero_informe = 1

numero_reporte = 1

while True:
    opcion = elegir_opcion()
    match opcion:
        case "1":
            validar(lista_empleados)
            escribir_empleados(lista_empleados)
            system ("cls")
        case "2":
            modificar_empleado(lista_empleados)
            system ("cls")
        case "3":
            eliminar_empleado(lista_empleados)
            escribir_empleados(lista_empleados)
            system ("cls")
        case "4":
            mostrar_todos(lista_empleados)
        case "5":
            calcular_promedio(lista_empleados)
            system ("cls")
        case "6":
            buscar_por_dni(lista_empleados)
            system ("cls")
        case "7":
            ordenar_empleados(lista_empleados)
            system ("cls")
        case "8":
            system("cls")
            numero_reporte = reporte(lista_empleados, numero_reporte)
            escribir_empleados(lista_empleados)
        case "9":
            numero_informe = buscar_por_apellido(lista_empleados, numero_informe)
            system("cls")
            system("cls")
        case "10":
            system("cls")
            print("Usted salio del Programa")
            system ("pause")
            system ("cls")
            break
