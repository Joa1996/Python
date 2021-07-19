class Persona:#Clase padre
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def __str__(self) : #Definimos este metodo para poder mostrar los objetos de esta clase
        return f'Persona: {self.nombre} {self.edad}'

class Empleado(Persona): #Clase Hija
    def __init__(self, nombre, edad,sueldo):
        super().__init__(nombre, edad)#Traemos los atributos de la clase padre
        self.sueldo=sueldo

empleado1=Empleado('Juan',25,5000)
#print(f'Objeto empleado1 : {empleado1 .nombre} {empleado1 .edad} {empleado1 .sueldo}   ') 
