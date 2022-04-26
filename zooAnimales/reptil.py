from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas: int = 0
    serpientes: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas: str = colorEscamas
        self._largoCola: int = largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        return cls.iguanas + cls.serpientes

    @classmethod
    def crearIguana(cls):
        pass

    @classmethod
    def crearSerpiente(cls):
        pass
    
    def movimiento(self):
        return ""

    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola