from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    _caballos: int = 0
    _leones: int = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje: bool = pelaje
        self._patas: int = patas

        Mamifero._mamiferos += 1

    @classmethod
    def cantidadMamiferos(cls):
        return cls.caballos + cls.leones

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        animalito = Mamifero(nombre, edad, "pradera", genero, True, 4)

        cls._caballos += 1
        cls._listado.append(animalito)

        return animalito

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        animalito =  Mamifero(nombre, edad, "selva", genero, True, 4)

        cls._leones += 1
        cls._listado.append(animalito)

        return animalito

    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas