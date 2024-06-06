"""CASO INVESTIGACIÓN CRIMINAL: CSI UTN 

Se ha encontrado una muestra de ADN en el lugar del crimen que contiene la siguiente secuencia de
bases nitrogenadas: “CGTTTAATG”. La investigación ha revelado tres posibles sospechosos, cada uno
con su propia muestra de ADN:
Juan Pérez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
María Rodríguez
Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
Carlos Sánchez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

Para resolver el caso, nos piden que desarrollemos un programa que compare las combinaciones de 
bases nitrogenadas de la muestra encontrada con las muestras de los sospechosos. 
Mostrar el nombre por pantalla en caso de encontrar al asesino, o la leyenda “SON TODOS INOCENTES”. 
"""

#Nombre: Lorenzo
#Apellido: Gomez Martins

from os import system

Juan = "CGGGGCTAAAATTTTTTACGATCG"
Maria = "AACGTTTAATGTTCTAAGCTGCG"
Carlos = "CGGGGCTAAAATTTTTTACGATCG"
ADN_sospechoso = "CGTTTAATG"

def Encontrar(cadena, subcadena):
    auxiliar = len(subcadena)
    for i in range (len(cadena)):
        if cadena [i : auxiliar + i] == subcadena:
            bandera = True
            break
    return bandera

def investigar():
    secuencia = "CGTTTAATG"
    mensaje = "TODOS LOS SOSPECHOSOS QUE HA INGRESADO SON INOCENTES"
    while True:
        sospechoso = input("ingrese el nombre del sospechoso: ")
        muestra_adn = input(f"ingrese la muestra del sospechoso {sospechoso}: ")
        validar = Encontrar(muestra_adn, secuencia)
        if validar == True:
            mensaje = f"{sospechoso} es el Culpable"
            break
        continuar = input("no hay coincidencia, desea ingresar otro sospechoso? ")
        system("cls")
        if continuar == "no":
            break

    print(mensaje)
    system("pause")
    system("cls")

csi = investigar()
