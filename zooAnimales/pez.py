from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    _salmones: int = 0
    _bacalaos: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas: str = colorEscamas
        self._cantidadAletas: int = cantidadAletas

        Pez._peces += 1
    
    @classmethod
    def cantidadPeces(cls):
        return cls.salmones + cls.bacalaos
    
    @classmethod
    def crearSamon(cls, nombre, edad, genero):
        animalito = Pez(nombre, edad, "oceano", genero, "rojo", 6)

        cls._salmones += 1
        cls._listado.append(animalito)

        return animalito

    @classmethod
    def crearBacalo(cls, nombre, edad, genero):
        animalito = Pez(nombre, edad, "oceano", genero, "gris", 6)

        cls._bacalaos += 1
        cls._listado.append(animalito)

        return animalito

    def movimiento(self):
        return ""

    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas