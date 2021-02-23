import sqlite3
import pandas as pd 
#Conectamos a la BD
conexion=sqlite3.connect('empresas.sqllite')#Nos conectamos a la BD, a la traves del nombre de esta
datos=pd.read_csv('C:/Users/Dell/Downloads/empresas-habilitadas.csv',header=0)#Leemos el dataframe del csv
df=pd.DataFrame(datos)#Pasamos a la variable df el dataframe
df.to_sql('empresashabilitadas',con=conexion)#Creamos una tabla empresashabilitadas y el driver automaticamente carga las tablas