import pandas as pd
datos=pd.read_csv('C:/Users/Dell/Downloads/Ingresos.csv',header=0)
print(datos)   
print(datos.iloc[0:3])#imprimir solo 3 filas
print(datos['anio'])#imprimir solo una columna
print(datos.sort_values(by='sexo'))#Ordenar
print(datos[datos.iloc[:,1]=='m'])#Usamos una condicion, es decir que nos muestre solo ciertos valores
sexo=datos['sexo']
print(sexo[sexo=='f'])#Otra alternativa de usar condicion
lista=datos['ingreso_ocup_principal']#Con esto pasamos una columna del csv a un array y de esta manera podemos extender las capacidades de operar sobre el csv
for y in range(len(lista)):
    print(lista[y])
prom=datos['ingreso_ocup_principal']
print("Promedio",prom.mean())#Calculamos el promedio de una columna
  
      