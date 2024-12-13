class Zoologico:
    
    def __init__(self, nombre, ubicacion, zonas):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def __init__(self):
        pass

    def agregarZonas(self,zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        animales = 0
        for i in self._zonas:
            numero = i.cantidadAnimales
            animales += numero
        return animales
    
    def getNombre(self):
        return self._nombre