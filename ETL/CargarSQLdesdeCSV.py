import pyodbc as pb
import pandas as pd

datos=pd.read_csv('D:\Practicas\ETL_Python\Prd05.csv',header=0)
df=pd.DataFrame(datos, columns=['ID','Prodcto'])
print(df)

conexion = pb.connect('Driver={SQL Server};'
                      'Server=DESKTOP-7A5VFUD\SQLSERVER;'
                       'Database=Destino;'
                      'Trusted_Connection=yes;')
cursor = conexion.cursor()

cursor.execute('CREATE TABLE PRDCSV (ID int, Prodcto nvarchar(10))') #Creamos la BD
conexion.commit()  
for row in df.itertuples(): #Creamos un For para que itere sobre cada una de las filas del Dataframe y ir cargando fila por fila a la BD
 cursor.execute('''
                INSERT INTO Destino.dbo.PRDCSV (ID, Prodcto)
                 VALUES (?,?)
                 ''',
                 row.ID,
                 row.Prodcto
     )
 #conexion.commit() 

cursor.execute('SELECT * FROM Destino.dbo.PRDCSV ')
for row in cursor:
     print(row)
conexion.commit() 