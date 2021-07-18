class Persona:
#     def __init__(self): #Metodo que se usa para crear los atributos de un objeto, es decir los atributos de la clase Persona
#         self.nombre='Juan'
#         self.edad =45
#     #pass#Palabra reservada para indicar que cree la funcion,en este caso la Clase, pero no va tener ningun contenido

# persona1=Persona() #De esta manera instanciamos un Objeto Persona, es decir creamos un objeto de la clase persona
# print(persona1.nombre)#Por ej. mostramos el nombre de nuestro objeto
    #Definimos el metodo para crear los atributos del objeto persona, pero esta vez los atributos seran asignados por parametros
    def __init__(self,nombre,apellido,edad): #Self se puede considerar como un puntero, que cuando instanciamos el objeto nos permite apuntar el mismo en la memoria, el nombre self puede ser cambiado por otro traquilamente
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    #Asignamos los metodos correspondientes a la clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}') #EN este caso usamos self debido a que es un metodo que esta en nuestra clase
     
  
persona1=Persona('Pablo','Lopez', 29)#En este caso lo que hace es llamar al metodo contructor de la clase (el metodo def__init) y el contructor nos pedira los respectivos parametros
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
persona1.mostrar_detalle() #llamamos el metodo del objeto para imprimir 
#Creamos otro objeto de la clase persona
#per2 es la variable que usamos para acceder al objeto Persona, Persona() es el objeto creado, que se encuentra en la memoria     
per2=Persona('Maria','Eder',31) #per2 es una variable que apunta al objeto que acabamos de instanciar
print(f'Objeto per2 : {per2.nombre} {per2.apellido} {per2.edad}') #una forma simple de imprimir los atributos de un objeto
#Recordar que cada vez que se intancia un objeto lo que se crea es un espacio de memoria reservada para que trabajemos con este objeto
#Python automaticamente elimina aquellos objetos que no se utilizan, esto se conoce como recolector de basura
#Sin embargo podemos usar lo siguiente si lo quisieramos realizar de manera manual para liberar recursos
del per2 #c/esto eliminamos a per2 que es la variable que apunta al objeto que se a creado
