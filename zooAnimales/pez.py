from zooAnimales.animal import Animal

class Pez(Animal):
    listado: [Pez] = []
    salmones: int = 0
    bacalaos: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas: str = colorEscamas
        self._cantidadAletas: int = cantidadAletas
    
    @classmethod
    def cantidadPeces(cls):
        return cls.salmones + cls.bacalaos
    
    @classmethod
    def crearSamon(cls):
        pass

    @classmethod
    def crearBacalo(cls):
        pass

    def movimiento(self):
        return ""

    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas