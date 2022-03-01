from Empleado import Empleado
from Gerente import Gerente
from Cabo import Cabo

'''
Otra alternativa para aplicar polimorfismo es generar en la clase padre en este caso
Empleado, un metodo (en este caso mostrardetalles) que hace lo mismo que en el caso anterior
pero sin la necesidad de tener que crear otra clase, es decir directamente en la clase padre
creamos el metodo al que le aplicaremos poliformismo, y posteriormente sus clases hijas
herederan este metodo
es otra forma de aplicar polimorfismo
'''


gerente=Gerente("Carlos","Sosa","Ejecutivo")
print(gerente.mostrardetalles())
print("--------")

empleado=Empleado("Marcos","Perez")
print(empleado.mostrardetalles())
print("--------")

cabo=Cabo("DIego","Funes",20154)
print(cabo.mostrardetalles())