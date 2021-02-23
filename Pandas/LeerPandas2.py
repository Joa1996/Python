import pandas as pd
datos=pd.read_csv('C:/Users/Dell/Downloads/Ingresos.csv',header=0)
print(datos.info()) #para saber las carateristicas del archivo csv, como la cant. de columnas
print(datos.iloc[[0,3],[1,2]])#De esta forma solo imprimimos las 3 primeras filas y solo 2 columnas 
Array=[datos]#Pasamos todo el dataframe o csv al array
for y in range(len(Array)):
    print(Array[y])
