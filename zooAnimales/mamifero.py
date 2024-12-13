from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,pelaje = None,patas = None):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)

    def crearCaballo(self,nombre,edad,genero):
        caballo = Mamifero(nombre, edad, "pradera",genero,True,4)
        self._listado.append(caballo)
        caballos += 1

    def crearLeon(self,nombre,edad,genero):
        leon = Mamifero(nombre, edad, "selva",genero,True,4)
        self._listado.append(leon)
        leones += 1

    def cantidadMamiferos(self):
        return len(self._listado)