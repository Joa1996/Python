"""
EN este ejemplo la idea es crear una clase Cubo, para luego instanciar objetos de ella
que calculen el volumen de un cubo

"""

class Cubo:

    def __init__(self,ancho,largo,profundidad):
        self.ancho=ancho
        self.largo=largo
        self.profundidad=profundidad

    
    def calc(self):
        Area=self.ancho*self.largo*self.profundidad
        return Area

ancho=int(input("Ancho"))
largo=int(input("Largo"))
prof=int(input("Profundidad"))

cub=Cubo(ancho, largo, prof)
print(cub.calc())

