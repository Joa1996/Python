import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Practicas\ETL_Python\Database1.accdb;')
cursor = conn.cursor()
cursor.execute('select * from table Tabla 1')
   
for row in cursor.fetchall():
    print (row)

#Para que funcione la conexion tanto Acces como Python debe ser de la misma arquitectura, es decir si
#Pthon es de 32 bits Acces tambien lo debe ser, si no se generara un error