from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,colorPiel = None,venenoso = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)

    def crearRana(self,nombre,edad,genero):
        rana = Anfibio(nombre, edad,"selva",genero,"rojo",True)
        self._listado.append(rana)
        ranas += 1

    def crearSalamandra(self,nombre,edad,genero):
        salamandra = Anfibio(nombre, edad, "selva",genero,"negro y amarillo",False)
        self._listado.append(salamandra)
        salamandras += 1

    def cantidadAnfibios(self):
        return len(self._listado)