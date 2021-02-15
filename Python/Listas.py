#Al igual que en otros lenguajes de programacion en py, tenemos las listas o arrays, estos permiten almacenar
#Datos de distintos tipos y acceder a ellos a  traves de subindices
#Declaracion
lista1=[1,2,3]
lista2=["Juan",23]
lista3=[] #Lista vacia
y=0
#Para recorrer una lista
for y in range(len(lista2)):
    print(lista2[y])
#Cargar datos en la lista
lista4=[]
m=0
tam=int(input("Ingrese la cantidad de numeros a cargar:"))
for m in range(tam):
    op=int(input("Ingrese el Numero:"))
    lista4.append(op)#Con append le decimos que todo elemento lo agregue al final del Array
#recorremos el Array
print("Imprimiendo lista cargada")
tt=0
for tt in range(len(lista4)):
    print(lista4[tt])
# Ej. Realizar la carga de valores enteros por teclado, almacenarlos en una lista. 
# Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista
lista5=[]
elemt=int(input("Ingrese un Entero:"))
while elemt!=0:
    lista5.append(elemt)
    elemt=int(input("Ingrese un Entero:"))#Esto es porque luego de que sea !0 va quedar dentro del while, por ende los siguientes elementos los tiene que cargar dentro del while
#Recorremos lo anterior
for z in range(len(lista5)):
    print(lista5[z])
