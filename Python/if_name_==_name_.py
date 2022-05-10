'''
main representa el nombre del modulo que el interprete de python esta ejecutando
entonces al hacer  if __name__ == '__main__' le estamos preguntando a python si esta ejecutando actualmente
este modulo o es otro importado.
Esto es util para los Scripts, ya que es una forma de saber que ese modulo de python contiene el Script. 
Ademas permite tener el control de todo el modulo desde un solo lugar, tambien se recomienda en caso de que el Modulo tenga 
muchos metodos, Usar un metodo Main que llame a todos los metodos de ese modulo
def main():
 saludoinicial()
 saludofinal()
'''

print("File __name__ : {}".format(__name__)) #imprimira name

def saludo():
    print("Hola")
if __name__ == "__main__":
     saludo()
else:
    print("No se puede ejecutar este metodo fuera del modulo original")
