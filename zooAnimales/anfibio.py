from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas: int = 0
    salamandras: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel: str = colorPiel
        self._venenoso: bool = venenoso

        Anfibio._anfibios += 1
    
    @classmethod
    def cantidadAnfibios(cls):
        return cls.ranas + cls.salamandras
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        animalito = Anfibio(nombre, edad, "selva", genero, "rojo", True)

        cls.ranas += 1
        cls._listado.append(animalito)

        return animalito

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        animalito = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

        cls.salamandras += 1
        cls._listado.append(animalito)

        return animalito

    def movimiento(self):
        return ""

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso