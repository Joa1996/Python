from abc import ABC,abstractclassmethod #Este modulo es necesiario importarlo para aplicar la Clase abstracta 
'''
Con las clases abstractas definimos una manera de definir una clase base, en la cual todas las
clases que hereden de esta tendran que tener todos sus atributos y metodos de manera obligatoria
es decir no es como en la herencia tradicional en la cual una clase puede tomar solo ciertos metodos
,en este caso si o si debe heredar todos sus atributos y metodos, estos nos puede servir para establecer
una clas padre unica, en la cual sus hijas deben mantener su estructura


En las clases abstractas no se pueden instanciar, esto provocara un error 
'''
class FiguraGemetrica(ABC):
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    #definimos el metodo Abstracto, por ende siempre se debe llamar la siguiente variable
    @abstractclassmethod
    def calculararea(self):
        pass
       #se le coloca un pass ya que en este caso el metodo es pasivo, es decir no hara nada como tal. 

class Cuadrado(FiguraGemetrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
    
    def calculararea(self):
        return self.alto*self.ancho


cu=Cuadrado(10,10)
print(cu.calculararea())

