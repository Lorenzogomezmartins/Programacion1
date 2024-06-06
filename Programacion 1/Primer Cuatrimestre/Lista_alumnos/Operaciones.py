from Validate import *
from os import system
import re
import json
from datetime import datetime
        
def mostrar_empleado(empleado: dict):
    print("***********************************************************************")
    Lista = "      ID       Nombre      Apellido     DNI      Puesto      Salario".split("|")
    print(Lista)
    print(f"{empleado["ID"]:>10}{empleado["Nombre"]:>12}{empleado["Apellido"]:>12}{empleado["DNI"]:>12}{empleado["Puesto"]:>12}{empleado["Salario"]:>12}")
    print("***********************************************************************")
    
def mostrar_todos(lista_empleados: list[dict]):
    for empleado in lista_empleados:
        mostrar_empleado(empleado)

def modificar_empleado (lista_empleados: list[dict]):
    ID_empleado = int(input("Ingrese el ID del empleado que quiera modificar: "))
    encontrado = False
    
    while True:
                opcion_modificar = input("""Que desea mofidicar\n1-Nombre: \n2-Apellido: \n3-DNI: \n4-Puesto: \n5-Salario: \n6-Salir\Elija una opcion: """).strip()
                for empleado in lista_empleados:
                    if empleado ["ID"] == ID_empleado:
                        encontrado = True
                        modificaciones = False
                        print("Alumno encontrado")
                        break

                match opcion_modificar:
                    case "1":
                        Nuevo_nombre = input("Ingrese el nuevo Nombre: ").capitalize()
                        if Nuevo_nombre and Nuevo_nombre.isalpha() and len(Nuevo_nombre) <= 20:
                            empleado["Nombre"] = Nuevo_nombre
                            modificaciones = True
                    case "2":
                        Nuevo_Apellido = input("Ingrese el nuevo Apellido: ").capitalize()
                        if Nuevo_Apellido and Nuevo_Apellido.isalpha() and len(Nuevo_Apellido) <= 20:
                            empleado["Apellido"] = Nuevo_Apellido
                            modificaciones = True
                    case "3":
                        Nuevo_DNI = int(input("Ingrese el nuevo DNI: "))
                        if 5000000 < Nuevo_DNI < 99999999:
                            empleado["DNI"] = Nuevo_DNI
                            modificaciones = True
                    case "4":
                        Nuevo_Puesto = input("Ingrese el nuevo Puesto: ").capitalize()
                        if Nuevo_Puesto in ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]:
                            empleado["Puesto"] = Nuevo_Puesto
                            modificaciones = True
                    case "5":
                        Nuevo_Salario = int(input("Ingrese el nuevo Salario: "))
                        if Nuevo_Salario > 234315:
                            empleado["Salario"] = Nuevo_Salario
                            modificaciones = True
                    case "6":
                        if modificaciones:
                            print("Se realizaron modificaciones.")
                        else:
                                print("No se realizaron modificaciones.")
                        return
                break


def eliminar_empleado (lista_empleado: list[dict]):
    ID_del_eliminado = int(input("Ingrese el ID del empleado que desea eliminar: "))
    empleado_eliminado = None
    for empleado in lista_empleado:
        if empleado["ID"] == ID_del_eliminado:
            print("Se encontro al alumno")
            empleado_eliminado = empleado

    if empleado_eliminado != None:
        lista_empleado.remove(empleado_eliminado)
    try:
        with open("Bajas.json", "r") as archivo:
            lista_eliminados = json.load(archivo)
    except:
        lista_eliminados = []

    lista_eliminados.append(empleado_eliminado)

    with open("Bajas.json", "w") as archivo:
        json.dump(lista_eliminados, archivo, indent=4)

    return empleado_eliminado
    

def calcular_promedio (lista_empleados: list[dict]):
    contador_salarios = 0
    cantidad_de_salarios = len(lista_empleados)
    for empleados in lista_empleados:
        contador_salarios += empleados["Salario"]
        promedio_salarios = contador_salarios / cantidad_de_salarios
        print(f"El promedio de los Salarios es: {promedio_salarios}")
        return promedio_salarios
    
def buscar_por_dni(lista_empleados: list[dict]):
    dni_empleados = int(input("Ingrese el DNI del empleado que desea ver: "))
    for empleado in lista_empleados:
        if empleado["DNI"] == dni_empleados:
            mostrar_empleado(empleado)

#####FUNCION ORDENAR#####
def ordenar_lista_ascendente(lista_empleados: list[dict], key):
    n = len(lista_empleados)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_empleados[j][key] > lista_empleados[j+1][key]:
                lista_empleados[j], lista_empleados[j+1] = lista_empleados[j+1], lista_empleados[j]

def ordenar_lista_descendente(lista_empleados: list[dict], key):
    n = len(lista_empleados)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_empleados[j][key] < lista_empleados[j+1][key]:
                lista_empleados[j], lista_empleados[j+1] = lista_empleados[j+1], lista_empleados[j]



def ordenar_empleados(lista_empleados: list[dict]):
    while True:
        Menu = input("\n1-Nombre: \n2-Apellido: \n3-Salario: \n4-Salir \nElija una opcion:")
        match Menu:
            case "1":
                decidir = input("Ingrese la opcion que desee ordenar: \n1 Ascendente: \n2 Dsescendente: ")
                match decidir:
                    case "1":
                        ordenar_lista_ascendente (lista_empleados, "Nombre")
                    case "2":
                        ordenar_lista_descendente (lista_empleados, "Nombre")
            case "2":
                decidir = input("Ingrese la opcion que desee ordenar: \n1 Ascendente: \n2 Dsescendente: ")
                match decidir:
                    case "1":
                        ordenar_lista_ascendente (lista_empleados, "Apellido")
                    case "2":
                        ordenar_lista_descendente (lista_empleados, "Apellido")
            case "3":
                decidir = input("Ingrese la opcion que desee ordenar: \n1 Ascendente: \n2 Dsescendente: ")
                match decidir:
                    case "1":
                        ordenar_lista_ascendente (lista_empleados, "Salario")
                    case "2":
                        ordenar_lista_descendente (lista_empleados, "Salario")
            case "4":
                system("cls")
                print("Opcion correcta")
                system ("pause")
                system ("cls")
        break


###############################ARCHIVOS#######################

def escribir_empleados (lista_empleados: list[dict]):
    with open("Empleados.csv", "w") as archivo:
        archivo.write("ID,Nombre,Apellido,DNI,Salario,Puesto\n")
        for empleado in lista_empleados:
            registro = f'{empleado["ID"]},{empleado["Nombre"]},{empleado["Apellido"]},{empleado["DNI"]},{empleado["Puesto"]},{empleado["Salario"]}\n'
            archivo.write(registro)

def leer_empleados(lista_empleados: list[dict]):
    try:
        with open("Empleados.csv", "r") as archivo:
            archivo.readline() 
            for linea in archivo:
                registro = linea.strip().split(",")
                diccionario = {
                    "ID": int(registro[0]),
                    "Nombre": registro[1],
                    "Apellido": registro[2],
                    "DNI": int(registro[3]),
                    "Puesto": registro[4],
                    "Salario": int(registro[5])
                }
                lista_empleados.append(diccionario)
    except:
        pass


def reporte(lista_empleados: list[dict], numero_reporte: int):
    sueldo_maximo = int(input("Ingrese el suelo maximo: "))
    empleados_superan_sueldo = [empleado for empleado in lista_empleados if empleado["Salario"] > sueldo_maximo]

    fecha_reporte = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_reporte = f"Reporte_{numero_reporte}.txt"

    with open(nombre_reporte, "w") as archivo:
            archivo.write(f"Reporte Número: {numero_reporte}\n")
            archivo.write(f"Fecha de Solicitud: {fecha_reporte}\n")
            archivo.write(f"Cantidad de Empleados que superan el sueldo {sueldo_maximo} = {len(empleados_superan_sueldo)}\n")
            archivo.write("Listado de Empleados:\n")
            archivo.write("ID, Nombre, Apellido, DNI, Puesto, Salario\n")

            for empleado in empleados_superan_sueldo:
                archivo.write(f"{empleado['ID']}, {empleado['Nombre']}, {empleado['Apellido']}, {empleado['DNI']}, {empleado['Puesto']}, {empleado['Salario']}\n")

            print(f"Reporte generado exitosamente: {nombre_reporte}")

    return numero_reporte + 1

def buscar_por_apellido(lista_empleados:list[dict], numero_informe: int):

    apellido_buscado = input("Ingese el apellido del empleado que quiera buscar: ")
    empleados_apellido = [empleado for empleado in lista_empleados if empleado["Apellido"] > apellido_buscado]
    
    fecha_informe = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_informe = f"Informe_{numero_informe}.txt"
    with open(nombre_informe, "w") as archivo:
        archivo.write(f"Informe Número: {numero_informe}\n")
        archivo.write(f"Fecha de Solicitud: {fecha_informe}\n")
        archivo.write(f"Cantidad de Empleados con el apellido {apellido_buscado}: {len(empleados_apellido)}\n")
        archivo.write("Listado de Empleados:\n")
        archivo.write("ID, Nombre, Apellido, DNI, Puesto, Salario\n")
        for empleado in empleados_apellido:
            archivo.write(f"{empleado['ID']}, {empleado['Nombre']}, {empleado['Apellido']}, {empleado['DNI']}, {empleado['Puesto']}, {empleado['Salario']}\n")

    return numero_informe
