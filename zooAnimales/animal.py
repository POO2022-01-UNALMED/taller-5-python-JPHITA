class Animal:
    _totalAnimales: int = 0

    _mamiferos: int = 0.
    _anfibios: int = 0
    _aves: int = 0
    _mamiferos: int = 0
    _peces: int = 0
    _reptiles: int = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre: str = nombre
        self._edad: int = edad
        self._habitat: str = habitat
        self._genero: str = genero
        self._zona = None

        Animal._totalAnimales += 1
    
    def movimiento(self):
        return ""
    
    @classmethod
    def totalPorTipo(cls):
        return F"Mamiferos : {cls._mamiferos}\nAves : {cls._aves}\nReptiles : {cls._reptiles}\nPeces : {cls._peces}\nAnfibios : {cls._anfibios}"

    def toString(self):
        r = F"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

        if self._zona != None:
            r += F"genero, la zona en la que me ubico es {self._zona.getNombre()}, en el {self._zona.getZoo().getNombre()}"

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