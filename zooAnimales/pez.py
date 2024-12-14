from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,colorEscamas = None,cantidadAletas = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)

    @classmethod
    def crearSalmon(self,nombre,edad,genero):
        salmon = Pez(nombre, edad,"oceano",genero,"rojo",6)
        self._listado.append(salmon)
        salmones += 1

    @classmethod
    def crearBacalao(self,nombre,edad,genero):
        bacalao = Pez(nombre, edad, "oceano",genero,"gris",6)
        self._listado.append(bacalao)
        bacalaos += 1

    def cantidadPeces(self):
        return len(self._listado)
    
    def getColorEscamas(self):
        return self._colorEscamas