num1=int(input("Ingrese la primera nota:"))
num2=int(input("Ingrese la segunda nota:"))
num3=int(input("Ingrese la tercera nota:"))
prom=(num1+num2+num3)/3
if(prom>=6):
    print("Alumno Aprobado")
else:
    print("Alumno Desaprobado")

print(prom)
print(type(prom)) #De esta manera podemos saber el tipo de dato que es la variable
print(len(str(prom)))#De esta manera podemos saber la cantidad de caracteres  de un numero, primero lo pasamos a un flujo de caracter y dpues recien podemos saber la cantidad de caracteres de ese flujo que representa un numero
numero=int(input("Ingrese un Numero Entero"))
#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.
if(len(str(numero))<=3):
    print("Correcto")
else:
    print("Ingreso un numero de mas de 3 cifras")