from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones: int = 0
    bacalaos: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas: str = colorEscamas
        self._cantidadAletas: int = cantidadAletas

        Animal._peces += 1
    
    @classmethod
    def cantidadPeces(cls):
        return cls.salmones + cls.bacalaos
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        animalito = Pez(nombre, edad, "oceano", genero, "rojo", 6)

        cls.salmones += 1
        cls._listado.append(animalito)

        return animalito

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        animalito = Pez(nombre, edad, "oceano", genero, "gris", 6)

        cls.bacalaos += 1
        cls._listado.append(animalito)

        return animalito

    def movimiento(self):
        return ""

    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas