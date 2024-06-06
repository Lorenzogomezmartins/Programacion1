#Nombre: Lorenzo
#Apellido: Gomez Martins

class boligrafo:
    def __init__(self, color, grosor):
        self.capacidad_tinta_maxima = 100
        self.cantidad_de_tinta = 80
        self.color = color
        self.grosor = grosor

    def escribir(self, texto: str):
        grosor = 1
        if self.grosor == "Grueso":
            grosor = 2
        cantidad_tinta_gasto = len(texto) * grosor
        if self.cantidad_de_tinta >= cantidad_tinta_gasto:
            retorno = texto 
            self.cantidad_de_tinta -= cantidad_tinta_gasto
            return retorno
        
    def recargar (self, cantidad: int):
        suma = self. cantidad_de_tinta + cantidad
        if suma > self.cantidad_de_tinta:
            self.cantidad_de_tinta = 100
            sobro = self.cantidad_de_tinta - suma
            cargo = f"Se cargo la lapicera y sobro: {sobro} cantidad de tinta"
        else:
            self. cantidad_de_tinta += cantidad
            cargo = "Lapicera cargada"
            return cargo

