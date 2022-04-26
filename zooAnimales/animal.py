from gestion.zona import Zona

class Animal:
    totalAnimales: int = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre: str = nombre
        self._edad: int = edad
        self._habitat: str = habitat
        self._genero: str = genero
        self._zona: [Zona] = []
    
    def movimiento(self):
        return ""
    
    @classmethod
    def totalPorTipo(cls):
        pass

    def __str__(self):
        pass

    def getNombre(self):
        return self._nombre
    def getEdad(self):
        return self._edad
    def getHabitat(self):
        return self._habitat
    def getGenero(self):
        return self._genero
    def getZona(self):
        return self._zona
    def setNombre(self, Nombre):
        self._nombre = Nombre
    def setEdad(self, Edad):
        self._edad = Edad
    def setHabitat(self, Habitat):
        self._habitat = Habitat
    def setGenero(self, Genero):
        self._genero = Genero
    def setZona(self, Zona):
        self._zona = Zona