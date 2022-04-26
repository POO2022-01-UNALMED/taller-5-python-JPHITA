from gestion.zoologico import Zoologico
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre, zoo = None):
        self._nombre: str = nombre
        self._zoo: Zoologico = zoo
        self._animales: [Animal] = []
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo
    def setNombre(self, Nombre):
        self._nombre = Nombre
    def setZoo(self, Zoo):
        self._zoo = Zoo