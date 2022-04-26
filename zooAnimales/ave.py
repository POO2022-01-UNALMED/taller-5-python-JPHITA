from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    _halcones: int = 0 
    _aguilas: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas: str = colorPlumas

        Ave._aves += 1

    @classmethod
    def cantidadAves(cls):
        return cls.halcones + cls.aguilas

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        animalito = Ave(nombre, edad, "montanas", genero, "cafe glorioso")

        cls._halcones += 1
        cls._listado.append(animalito)

        return animalito

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        animalito = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

        cls._aguilas += 1
        cls._listado.append(animalito)

        return animalito

    def movimiento(self):
        return ""

    def getColorPlumas(self):
        return self._colorPlumas