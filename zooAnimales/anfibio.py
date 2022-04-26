from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado: [Anfibio] = []
    ranas: int = 0
    salamandras: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel: str = colorPiel
        self._venenoso: bool = venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return cls.ranas + cls.salamandras
    
    @classmethod
    def crearRana(cls):
        pass

    @classmethod
    def crearSalamandra(cls):
        pass

    def movimiento(self):
        return ""

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso