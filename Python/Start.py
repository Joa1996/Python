import math #Al igual que en Java debemos importar las librerias que querramos usar
print("Hola")#Imprimir o mostrar en pantalla
#Python se considera como lenguaje interpretado porque los programas de Python 
#se ejecutan por medio de un interprete. Existen dos maneras de usar el interprete: modo de comando 
#y modo de guion. En modo de comando se escriben sentencias en el lenguaje Python y 
#el interprete muestra el resultado.Con el modo comando podemos ejecutar comandos python sin necesidad de guardar
#, cuando tenemos los siguientes simbolos estamos en modo comando <<<, mientras que en modo guion es cuando escribimos
#un archivo en python para guardarlo posteriormente y ecejutarlo  desde el archivo
#Declaracion de variables
a="HOla"
b = 8 
c = 8
print (a)
print (b+c)
#Los nombres de las variables pueden tener una longitud arbitraria. Pueden estar
#formados por letras y numeros, pero deben comenzar con una letra, aceptable usar mayusculas, por convenci´on no lo hacemos. Si lo hace, recuerde
#que la distinci´on es importante: Bruno y bruno son dos variables diferentes.
#El gui´on bajo ( ) tambi´en es legal y se utiliza a menudo para separar nombres
#con m´ ultiples palabras, como mi nombre o precio del cafe colombiano.
#Si intenta darle a una variable un nombre ilegal, obtendr´a un error de sintaxis.
#Lo que nunca podremos usar como variable en python son las siguientes palabras reservadas:
# and       continue    else     for     import   not     raise
# assert    def         except   from    in        or     return
# break     del         exec     global  is        pass    try
# class     elif        finally  if      lambda    print   while
#Sentencias, pueden ser de asignacion o de salida, de asignacion ej: x=2 de salida print
#OperadoresyExpresiones
#Ej: 20+32  hora-1   hora*60+minuto   minuto/60 5**2(representa 5^2)   (5+9)*(15-7)
x=5
b=10
c=(10*5)**2
print(c)
#Cada valor tiene un id, que es un valor unico ´ relacionado con d´onde se almacena
#en la memoria del computador. El id de una variable es el id del valor al que
#hace referencia.
id(x)#Probar  en modo de comando
#Conversion de tipos
print(int("32")+1)
print(int(3.9852))#Python siempre redondea hacia abajo
print(float(3))#C/esto convertimos de enteros a decimales
print(str(33))#C/esto convertimos a datos de tipo String
print(math.log10(17))
#Python define tres tipos de datos numéricos básicos: enteros(int), números de punto flotante(float) y numeros complejos (complex)
#Estructuras logicas
#if
sueldo=int(input("Ingrese su sueldo")) #de esta manera podemos ingresar datos por consola 
if sueldo > 20000:
    print("Su sueldo es elevado")
else:
    print("Su sueldo es bajo")   
#Todo lo que se encuentre en la rama del verdadero del if se debe disponer a 4 espacios corrido a derecha.
#La indentación es una característica obligatoria del lenguaje Python para codificación de las estructuras condicionales, de esta forma el intérprete de Python puede identificar donde finalizan las instrucciones contenidas en la rama verdadera del if.
num=int(input("Ingrese un numero:"))#Con el int transformamos el flujo de String a int
if num!=0:
    print(num*10)
else:
    print("No igual")
#Ej. de estructuras condicionales complejas
