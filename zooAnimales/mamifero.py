from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,pelaje = False,patas = None):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        caballo = Mamifero(nombre, edad, "pradera",genero,True,4)
        cls._listado.append(caballo)
        Mamifero.caballos += 1

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        leon = Mamifero(nombre, edad, "selva",genero,True,4)
        cls._listado.append(leon)
        Mamifero.leones += 1

    def cantidadMamiferos(self):
        return len(self._listado)
    
    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas