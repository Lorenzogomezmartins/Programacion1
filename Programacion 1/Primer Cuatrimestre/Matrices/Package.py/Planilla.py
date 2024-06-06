from Legajos import *
from os import system
from input import *

def crear ():
    planilla = [[0]* 5 for _ in range(3)]
    return planilla

def cargar_datos (planilla):
    legajos = armar_legajos( )
    legajo_ingresado = comprabar(legajos)
    if legajo_ingresado == False:
        linea = get_int(" Ingrese una linea: ", "linea incorrecta", 1, 3)
        coche = get_int(" Ingrese un coche: ", "Coche incorrecto", 1, 5)
        recaudacion = int(input("Ingrese la recaudacion: "))
        planilla[linea - 1][coche - 1] += recaudacion
        print("Los datos se han cargado con exito")

        system(" pause ")
        system(" cls ")
