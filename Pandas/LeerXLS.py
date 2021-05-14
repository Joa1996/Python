import pandas as pd
xls=pd.ExcelFile('D:/Practicas/ETL_Python/Compras.xlsx')
print(xls.sheet_names) #Imprimimos las hojas del excel 
df=xls.parse('Principal')#Cargamos lo de la hoja 1 a un dataframe, para posteriormente imprimirlo
print(df)