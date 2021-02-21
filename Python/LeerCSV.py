import csv
ruta='C:/Users/Dell/Downloads/catalogo.csv'#ruta donde se aloja el csv
with  open(ruta, encoding='latin1') as csvarchivo:
      entrada=csv.reader(csvarchivo)
      for reg in entrada: #Recorremos todos las filas del csv y los imprimimos
          print(reg)
csvarchivo.close()



     
     
  

