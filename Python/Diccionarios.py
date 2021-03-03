#Los diccionarios son una alternativa a las listas, permite almacenar elementos de cualquier tipo de forma desordenada, ademas cada uno de 
#los elementos almacenados tienen una clave, es decir cada elemento se almacena con una respectiva clave.
#Declaracion de diccionarios
diccionario= {1:"Hernesto",2:"Juan",3:"Pablo"}# En este caso la clave es el numero y el valor los nombres
print(diccionario)
#Si queremos imprimir solo un elemento tan solo llamamos a su clave
print(diccionario[1])
#A su vez podemos introducir un diccionario dentro de otro diccionario
diccionario2={1:"Pantalon",2:{1:"Botones",2:"Borcegos"},3:"Zapatillas"}
print(diccionario2)
print(diccionario2[2])