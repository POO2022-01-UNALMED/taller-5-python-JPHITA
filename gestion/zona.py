from gestion.zoologico import Zoologico
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre, zoo = None):
        self.nombre: str = nombre
        self.zoo: Zoologico = zoo
        self.animales: [Animal] = []
    
    def agregarAnimales(self, animal):
        self.animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self.animales)

    def getNombre(self):
        return self._Nombre
    def getZoo(self):
        return self._Zoo
    def setNombre(self, Nombre):
        self._nombre = Nombre
    def setZoo(self, Zoo):
        self._zoo = Zoo