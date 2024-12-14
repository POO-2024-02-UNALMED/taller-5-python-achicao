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
    def crearSalmon(cls,nombre,edad,genero):
        salmon = Pez(nombre, edad,"oceano",genero,"rojo",6)
        Pez.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        bacalao = Pez(nombre, edad, "oceano",genero,"gris",6)
        Pez.bacalaos += 1
        return bacalao

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas