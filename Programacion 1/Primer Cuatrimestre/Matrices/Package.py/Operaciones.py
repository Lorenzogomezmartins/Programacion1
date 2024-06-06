from os import system

def mostrar_coches_lineas (planilla):
    print("Mostrar la recaudacion total de todos los coches: ")
    for i in range (len(planilla)):
        print(f" linea {i + 1}: ", end = " ")
        for j in range (len(planilla [0])):
            auxiliar = planilla[i][j]
            print(f"coche {j + 1}: ${auxiliar : 5}", end= " ")
            print("")
    system(" pause ")
    system(" cls ")

def mostar_recaudacion_por_linea (planilla):
    print("Recaudacion por linea:")
    for i in range(len(planilla)):
        suma = 0
        for j in range(len(planilla[0])):
            suma += planilla[i][j]
        print(f"linea {i + 1}: ${suma : 5}", end= " ")
        print()
    system("pause")
    system("cls")

def mostrar_por_coche(planilla):
    print("recaudacion por coche:")
    for i in range(len(planilla[0])):
        suma = 0
        for j in range(len(planilla)):
            suma += planilla[j][i]
        print(f"coche {i + 1}: ${suma : 5}", end= " ")
        print()
    system("pause")
    system("cls")
def recaudacion_total (planilla):
    suma = 0
    for i in range (len(planilla)):
        for j in range (len(planilla[0])):
            suma += planilla[i][j]
    print(f"La Recaudacion total fue de: ${suma}", end = " ")
    print("")
    system (" pause ")
    system (" cls ")
    