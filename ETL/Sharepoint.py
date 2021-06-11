#Con este script la idea es poder descargar archivos contenidos en un Sharepoint
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
import os
import tempfile
site_url= 'https://empresa.sharepoint.com/sites/Test' #URL del Sharepoint
ctx = ClientContext(site_url).with_credentials(UserCredential("usuario","contraseña"))#Credenciales del Sharepoint

file_url='/sites/Test/Documentos compartidos/Vtas(prueba).xlsx' #Pasamos la Otra parte  del Sharepoint donde esta el recurso, fijarse de tener en cuenta los espacios en la URL
ruta='C:/Users/Dell/Downloads' #Establecemos la ruta donde queremos que nos descargue el Excel 
download_path = os.path.join(ruta, os.path.basename(file_url))

with open(download_path, "wb") as local_file:
     file = ctx.web.get_file_by_server_relative_path(file_url).download(local_file).execute_query()
print("[Ok] file has been downloaded: {0}".format(download_path))
