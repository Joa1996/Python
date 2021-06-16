#La idea aqui es poder remplazar valores que no queremos en un Dataframe, que podrian por ej. molestar al cargarlo a otra BD, como una caracter especifico, etc.
import pandas as pd
#Cargamos un DF de ejemplo
df=pd.DataFrame({ 'X': [1, 2, '/', 4, 5],  
                  'Y': [5, 6, 7, 8, 9],  
                  'Z': ['"', 'y', 'a', 'b', 'c']})
print(df)#imprimos como esta el DF original
remplazo=df.replace(to_replace='"',value='') #Usamos la funcion replace de Pandas, en to_replace pasamos el valor a remplazar y en value por lo que queremos remplazar
#Imprimimos el ejemplo
#print(remplazo)
#De esta manera le decimos que remplaze a varios valores
remplazo2=df.replace(to_replace=['"','/'],value='') 
#print(remplazo2)
#Otras maneras de reemplazar en un DF
remplazo3=df.replace(to_replace={5:'q','a':2},value=None)
#print(remplazo3)
#Remplazar una columna especifica
remplazo4=df.replace(to_replace={'X':{5:50}},value=None) #En este caso solamente reemplazar el 5 por el 50 en la columna X
#print(remplazo4)
remplazo5=df.replace(to_replace={'X' : {5:50},
                                 'Y' : {5:60}},value=None)
print(remplazo5)                                 
#En este ultimo le podemos decir varias columnas a reemplazar