class Animal():
    _totalAnimales = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,zona = None):
        self._nombre = nombre
        self.edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1
    
    def movimiento(self):
        return "desplazarse"
    
    @staticmethod
    def totalPorTipo(self):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio

        return f"Mamiferos: {Mamifero.cantidadMamiferos}\nAves: {Ave.cantidadAves}\nReptiles: {Reptil.cantidadReptiles}\nPeces: {Pez.cantidadPeces}\nAnfibios: {Anfibio.cantidadAnfibios}"

    def __str__(self):
        
        if self._zona != None:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona[0]}, en el {self.zona[0].getZoo().getNombre()}"
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"   
        