from Empleado import Empleado
from Gerente import Gerente
from Cabo import Cabo

#Definimos un metodo que sera el que aplicara polimorfismo, este metodo tendra la
#capacidad de que le pasemos como parametro un objeto que estemos instanciando
#y poder imprimir todos los detalles de este objeto que se esta instanciando
#Esto es polimorfismo usamos un solo metodo  para ejecutarlo con distintos objetos instanciados
#y correra en tiempo de ejecucion
#De esta manera estamos reutilizando un mismo metodo que se puede usar en las distintas clases
#y nos evitamos tener que crear este metodo en cada una de las clases
def imprimir_detalles(objeto): #le pasamos como atributo el objeto instanciado
    print(objeto)
    print(type(objeto))
    if isinstance(objeto,Gerente):#Es una manera de obtener los atributos de un objeto, preguntamos si el objeto al que estamos instanciando es Gerente y queremos que nos traiga de este el atributo Puesto
        print(objeto.Puesto)#Tambien podriamos usar esto para saber si un objeto pertenece o no cierto objeto

gerente=Gerente("Carlos","Sosa","Ejecutivo")
imprimir_detalles(gerente)
print("--------")

empleado=Empleado("Marcos","Perez")
imprimir_detalles(empleado)
print("--------")

cabo=Cabo("DIego","Funes",20154)
imprimir_detalles(cabo)
