import pyodbc as pb
conexion = pb.connect('Driver={SQL Server};'
                      'Server=Nombre Servidor;'
                      'Database=Nombre BD;'
                      'Trusted_Connection=yes;')
cursor = conexion.cursor()
cursor.execute('SELECT * FROM Destino.dbo.Compras') #Ejecutamos una query
for row in cursor:
    print(row)#

