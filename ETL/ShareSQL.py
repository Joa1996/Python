#C/este Script lo que vamos ahace es descargar un Excel de un sharepoint y cargarlo a slq server
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
import os
import tempfile


site_url= 'https://Empresa.com/sites/CLIENTES-MERCADOS' #URL del Sharepoint
ctx = ClientContext(site_url).with_credentials(UserCredential("Usuario","Contraseña"))#Credenciales del Sharepoint

file_url='/sites/CLIENTES-MERCADOS/Documentos compartidos/Clientes - Mercados.xlsx' #Pasamos la Otra parte  del Sharepoint donde esta el recurso, fijarse de tener en cuenta los espacios en la URL
ruta='C:/Users/Dell/Downloads' #Establecemos la ruta donde queremos que nos descargue el Excel 
download_path = os.path.join(ruta, os.path.basename(file_url))

with open(download_path, "wb") as local_file:
     file = ctx.web.get_file_by_server_relative_path(file_url).download(local_file).execute_query()
print("[Ok] file has been downloaded: {0}".format(download_path))

 #Ahora cargamos el Excel que se descargo del Sharepoint a un DataFrame 
df= pd.read_excel (r'C:/Users/Dell/Downloads/Vtas(prueba).xlsx', sheet_name='Hoja1')
print (df)
 #COnectamos a nuestra BD
conexion = pb.connect('Driver={SQL Server};'
                      'Server=Nombre SErvidor;'
                      'Database=Destino;'
                      'Trusted_Connection=yes;')
cursor = conexion.cursor()
#Procedemos a cargar todos los registros del Excel a nuestra tabla
for row in df.itertuples():
          #print(row)
     cursor.execute('''
                  INSERT INTO Destino.dbo.Ventas_Prueba(Vendedor, Total, Total_Vendida )
                   VALUES (?,?,?) 
                   ''',
                   row.Vendedor,
                   row._2, #El metodo intertuples me toma a la columna Total y Total_Vendida como _2 y _3 respectivamente
                   row._3
                   )

conexion.commit() 