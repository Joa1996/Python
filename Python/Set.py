'''
Son otro tipo de coleccion disponible en Python,las colecciones Set no mantienen un orden, no permiten ingresar elementos
duplicados, los elementos ingresados no se pueden modificar, pero si se pueden eliminar o agregar mas elementos
Esta coleccion es muy util si queremos almacenar elementos unicos que no se repitan
'''

#Definimos una coleccion SET que contendra planetas
planetas = {'Marte','Venus','Jupiter'}
print(planetas)#Como no mantiene el orden puede ir variando el orden en que se muestran los planetas
#Conocer el tamaño del Set
print(len(planetas))
#Saber si un elemento esta presente en la coleccion Set
print('Marte' in planetas)#Esto se puede realizar tanto para tuplas como para listas
print('Ricardo' in planetas)#Devolvera False
#Agregar elementos en la coleccion Planetas
planetas.add('Tierra')
print(planetas)
#Como no soporta elementos duplicados no cargara este ultimo
planetas.add('Tierra')
print(planetas)#Mostrara solo el que se ingreso anteriormente
#Eliminar elementos dentro de la coleccion
planetas.remove('Tierra')
print(planetas)
#Limpiar Coleccion de manera completa
planetas.clear()
print(planetas)
#Eliminar directamente la variable
del planetas