#While
x=1
while x<=10:
    print(x)
    x=x+1#En esta parte termina el bucle while, por ende todo lo que siga dpues debe ir a la isq.
print("test fuera del while")#como por ej. esto
#Otro ej. en este caso calculamos los multiplos de 8 hasta el 62
n=8
while n<=62:
    print(n)
    n=n+8
#For
#Hay varias formas de usar el For, una de ellas es con la funcion range(), en esta podemos decirle que recorra una variable una determinada cant. de veces dentro del parentesis
y=1
for y in range(50):
    print(y) 
#inclusive podemos especificar el rango, por ej que recorra desde el  rango 1 al 11 cada 3 veces, lo que hara sera sumar a partir del 1 el 3, por ej. (3+1) luego a eso (4+3) y asi sucesivamente hasta llegar al 11 
for  m in range(1,11,3):
    print(m)
#podemos usar range() por ej. para permitir el ingreso de 10 numeros y sumarlos
sum=0
for num in range(10):
    i=int(input("Ingrese el numero"))
    sum=sum+i
print("La suma es:"+str(sum))#Imprimimos fuera del for para que no se repita, py bo es como java, para concatenar todas las variables tienen que ser del mismo tipo, en este caso String
#Ej. de Ejercicio, Codificar un programa que lea n números enteros y 
# calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)
p=int(input("Ingrese la Cantidad de numeros enteros que ingrsara:"))
s=0
suma=0
for s in range(p):
    qo=int(input("Ingrese el Nmero:"))
    if qo>=1000:
        suma=suma+1
print(suma)

