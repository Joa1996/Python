class Aritmetica:
    """    
    Para comentar en varias lineas
    """
    def __init__(self,varA,varB): #Definimos los atributos de la clase
        self.varA=varA
        self.varB=varB
    def suma(self):
        return self.varA+self.varB
    def resta(self):
         return self.varA-self.varB
    def multi(self):
        return self.varA*self.varB
ari=Aritmetica(2,5)
print(ari.suma())
print(ari.resta())
print(ari.multi())