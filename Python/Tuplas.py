'''
Las tuplas son una alternativa de colecion de datos, a diferencia de las listas o diccionarios, las tuplas
son mas restrictivas. Por ej. una vez que definimos una tupla no podemos modificarla agregando mas
elementos o eliminar los elementos de esta
Las tuplas  se conocen como inmutable (No modificable)
'''

#Definir una tupla
frutas=('Naranja','Manzana','Banana')
Comida=('Arroz',23)
#largo de una tupla
print(len(frutas))
#Acceder a un rango
print(frutas[0:2])
#Convertir  tupla a una lista
frutalista=list(frutas)
