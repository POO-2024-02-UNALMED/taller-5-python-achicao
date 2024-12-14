from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,colorEscamas = None,largoCola = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(self)

    @classmethod
    def crearIguana(self,nombre,edad,genero):
        iguana = Reptil(nombre, edad,"humedal",genero,"verde",3)
        self._listado.append(iguana)
        Reptil.iguanas += 1

    @classmethod
    def crearSerpiente(self,nombre,edad,genero):
        serpiente = Reptil(nombre, edad, "jungla",genero,"blanco",1)
        self._listado.append(serpiente)
        Reptil.serpientes += 1

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola