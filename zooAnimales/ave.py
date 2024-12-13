from zooAnimales.animal import Animal


class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,colorPlumas = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorPlumas
        self._listado.append(self)

    def crearHalcon(self,nombre,edad,genero):
        halcon = Ave(nombre, edad,"montañas",genero,"cafe glorioso")
        self._listado.append(halcon)
        halcones += 1

    def crearAguila(self,nombre,edad,genero):
        aguila = Ave(nombre, edad, "montañas",genero,"blanco y amarillo")
        self._listado.append(aguila)
        aguilas += 1

    def cantidadAves(self):
        return len(self._listado)
    
