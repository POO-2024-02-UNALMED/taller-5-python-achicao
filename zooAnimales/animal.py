class Animal():
    _totalAnimales = 0

    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1
    
    def movimiento(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio

        return (f"Mamiferos : {Mamifero.cantidadMamiferos()}\n"
                f"Aves : {Ave.cantidadAves()}\n"
                f"Reptiles : {Reptil.cantidadReptiles()}\n"
                f"Peces : {Pez.cantidadPeces()}\n"
                f"Anfibios : {Anfibio.cantidadAnfibios()}")

    def toString(self):
        
        if self._zona != None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.getZoo().getNombre()}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"   
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self,edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self,habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self,genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    
    def setZona(self,zona):
        self._zona = zona