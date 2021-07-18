'''
Metodos Getter and Setter, en este caso definimos un objeto Persona, al que le pasaremos los parametros por el metodo
Set, y obtendremos los atributos de este objeto con su metodo Get.
Es una practica uy comun para lograr el encapsulamiento de un objeto
Encapsular los datos de una aplicación significa evitar que se le de acceso
Para ello, se crea una estructura que contiene métodos que pueden ser utilizados por cualquier
otra clase, sin causar incoherencias en el desarrollo de código.
Esto es lo que en Java se logra con los modificadores de Acceso Private, public y Protected, Python a diferencia
de Java es mas permisible. 
'''
class Persona:
    def __init__(self):
        self._nombre=''#El gion bajo antes del nombre representa encapsulamiento
        self._apellido=''

    #Metodo Get
    @property #esto es necesario para definir el metodo Get
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    
    #Metodo Setter
    @nombre.setter #esto es necesario para definir el metodo Set
    def nombre(self,nombre):
        self._nombre=nombre
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido
'''
Con los Getter and setter, entre otras cosas podemos lograr el encapsulamiento, ya que por ej. al eliminar el metodo
Setter solo se podra leer los atributos del objeto, no asi modificarlos o asignarlos.
'''
#Creamos un objeto
per1=Persona()
per1.nombre='Diego'
per1.apellido='Lopez'

print(f'Objeto per1 : {per1.nombre} {per1.apellido}') 
print(__name__)