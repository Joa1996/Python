import json

with open('configuracion.json') as f:
   data = json.load(f)

#de lo que levantamos de nuestro JSON lo  cargamos a variables que posteriormente usaremos
puerto=data['puerto']
tipo=data['tipo']


print(puerto,tipo)