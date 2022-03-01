from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, Nombre, Apellido,Puesto):
        super().__init__(Nombre, Apellido)
        self.Puesto=Puesto
    
    def __str__(self):#Sobre escribimos el metodo de la clase padre y le agregamos la descripcion del gerente
        return super().__str__()+f'Gerente [Puesto:{self.Puesto}'

