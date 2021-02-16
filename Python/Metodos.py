#Con los metodos viene el concepto de La programación estructurada, esta  busca dividir o 
# descomponer un problema complejo en pequeños problemas. 
# La solución de cada uno de esos pequeños problemas nos trae la solución del problema complejo
#En Python el planteo de esas pequeñas soluciones al problema complejo se hace dividiendo el programa en funciones
#Una función es un conjunto de instrucciones en Python que resuelven un problema específico.
#El lenguaje Python ya tiene incorporada algunas funciones básicas. 
# Algunas de ellas ya las utilizamos y son:  print, len y range
# Para declarar un metodo se utiliza def metodo():
#el nombre de la función (el nombre de la función no puede tener espacios en blanco, comenzar con un número y el único caracter especial permitido es el _ )
def saludo():
    print("Probando Metodos")
def calculo():
    n=int(input("Ingrese un numero"))
    print(n*100)
#Metodo con parametros
def Area_Cuadrado (base,altura):
    cal=base*altura
    return cal
def Mayor(num1,num2):
    if num1>num2:
        mayor=num1
    else:
        mayor=num2    
    return mayor    
#Funcion Con parametros en forma de lista
def sumatoria(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
#llamamos a los metodos anteriores, aqui enpieza realmente el programa, el orden con el que llamamos a los metodos es importante en este caso primero queremos que salude y dpues que calcule
saludo()
calculo() #Para que los metodos funcionen si o si deben ser llamados de esta forma
#Llamar metodo con parametro
b=int(input("Ingrese la base del cuadrado:"))
a=int(input("Ingrese la altura del cuadrado:"))
print(Area_Cuadrado(b,a))
#Otra Alternativa
ll=Area_Cuadrado(a,b)
print(ll)
# Ej. Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor
n1=int(input("Ingrese el primer numero"))
n2=int(input("Ingrese el segundo numero"))
print(Mayor(n1,n2))
#Pasamos parametros en forma de lista al metodo "sumatoria"
lista=[10,100,100,300]
print(sumatoria(lista))
