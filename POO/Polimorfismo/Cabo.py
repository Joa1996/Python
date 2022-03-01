from Empleado import Empleado

class Cabo(Empleado):
    def __init__(self, Nombre, Apellido,Sueldo):
        super().__init__(Nombre, Apellido)
        self.Sueldo=Sueldo
    def __str__(self):
        return super().__str__()+f'Cabo [Sueldo:{self.Sueldo}'
