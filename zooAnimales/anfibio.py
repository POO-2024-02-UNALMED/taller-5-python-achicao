from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,colorPiel = None,veneno = False):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel = colorPiel
        self._veneno = veneno
        self._listado.append(self)

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        rana = Anfibio(nombre, edad,"selva",genero,"rojo",True)
        Anfibio.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra = Anfibio(nombre, edad, "selva",genero,"negro y amarillo",False)
        Anfibio.salamandras += 1
        return salamandra

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def getColorPiel(self):
        return self._colorPiel
    
    def isVenenoso(self):
        return self._veneno