from zooAnimales.animal import Animal


class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,colorPlumas = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorPlumas
        self._listado.append(self)

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        halcon = Ave(nombre, edad,"montañas",genero,"cafe glorioso")
        Ave.halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        aguila = Ave(nombre, edad, "montañas",genero,"blanco y amarillo")
        Ave.aguilas += 1
        return aguila

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    def getColorPlumas(self):
        return self._colorPlumas