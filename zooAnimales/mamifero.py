from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos: int = 0
    leones: int = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje: bool = pelaje
        self._patas: int = patas

    @classmethod
    def cantidadMamiferos(cls):
        return cls.caballos + cls.leones

    @classmethod
    def crearCaballo(cls):
        pass

    @classmethod
    def crearLeon(cls):
        pass

    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas