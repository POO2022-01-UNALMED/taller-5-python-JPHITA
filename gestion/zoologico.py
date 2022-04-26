from gestion.zona import Zona

class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre: str = nombre
        self._ubicacion: str = ubicacion
    

    def agregarZonas(self, nuevaZona):
        self._Zonas.append(nuevaZona)
        nuevaZona.setZoo(self)

    @classmethod
    def cantidadTotalAnimales(cls):
        pass

    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def setNombre(self, nombre):
        self._nombre = nombre
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion