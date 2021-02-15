#Para los datos de tipo string podemos saber la posicion que ocupa una letra de la siguiente manera:
nom="Pedro"
print(nom[4])#mostraria la om de esta manera podriamos trabajar por ej. para comparar las inciales de nombres
#Solicitar la carga del nombre de una persona en minúsculas.
# Mostrar un mensaje si comienza con vocal dicho nombre.
nombre=input("Ingrese su Nombre:")
if nombre[0]=="a" or nombre[0]=="e" or nombre[0]=="i" or nombre[0]=="o" or nombre[0]=="u":
    print("Su nombre comienza con Vocales")
else:
    print("Su nombre no comienza con Vocales")

#Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".
tt=0
mail=input("Ingrese su email")
for m in range(len(mail)):
    if mail[m]=="@":
        tt=tt+1

if tt>=1:
    print("Correcto")
else:
    print("incorrecto, debe ingresar un mail")
   
    
