from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas: int = 0
    serpientes: int = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas: str = colorEscamas
        self._largoCola: int = largoCola

        Animal._reptiles += 1
    
    @classmethod
    def cantidadReptiles(cls):
        return cls.iguanas + cls.serpientes

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        animalito = Reptil(nombre, edad, "humedal", genero, "verde", 3)

        cls.iguanas += 1
        cls._listado.append(animalito)

        return animalito

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        animalito = Reptil(nombre, edad, "jungla", genero, "blanco", 1)

        cls.serpientes += 1
        cls._listado.append(animalito)

        return animalito
    
    def movimiento(self):
        return ""

    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola