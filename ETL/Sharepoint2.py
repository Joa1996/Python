#C/este Script podemos cargar archivos a un sharepoint
import os
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
import test
#URL del Sharepoint
site_url= 'https://Empresa.sharepoint.com/sites/Test'

ctx = ClientContext(site_url).with_credentials(UserCredential("Usuario","Pass"))
path= 'D:/Practicas/ETL_Python/JunioVtas.CSV.txt'

with open(path, 'rb') as content_file:
    file_content = content_file.read()

list_title = "Documentos"
target_folder = ctx.web.lists.get_by_title(list_title).root_folder
name = os.path.basename(path)
target_file = target_folder.upload_file(name, file_content)
ctx.execute_query()
print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))
