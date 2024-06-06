#Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.
#Nombre: Lorenzo
#Apellido: Gomez Martins

def reemplazar_nombres (lista: list, nombre: str, reemplazo: str):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == reemplazo:
            lista[i] = nombre
            contador += 1

    print(lista)
    return contador

lista_de_nombres = ["José", "Juan", "Lorenzo", "Germán", "Anabella", "Valeria", "Luciana"]
#reemplazodo =  get_str ("Ingrese el nombre que quiera reemplazar: ")
#nombre_puesto = get_str ("Ingrese el nombre que quiera poner, 100, 2")

#final = reemplazar_nombres (lista_de_nombres , reemplazodo, nombre_puesto)
#print(final)