from zooAnimales.animal import Animal

class Ave(Animal):

    listado: [Ave] = []
    halcones: int = 0 
    aguilas: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas: str = colorPlumas

    @classmethod
    def cantidadAves(cls):
        return cls.halcones + cls.aguilas

    @classmethod
    def crearHalcon(cls):
        pass

    @classmethod
    def crearAguila(cls):
        pass

    def movimiento(self):
        return ""

    def getColorPlumas(self):
        return self._colorPlumas