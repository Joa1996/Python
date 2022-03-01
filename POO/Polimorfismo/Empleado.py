class Empleado:
    def __init__(self,Nombre,Apellido):
        self.Nombre=Nombre
        self.Apellido=Apellido

    def __str__(self):
        return f'Empleado: [Nombre:{self.Nombre},Apellido:{self.Apellido}]'  
    
    def mostrardetalles(self):
        return self.__str__()
  
    