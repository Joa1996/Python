'''
main representa el nombre del modulo que el interprete de python esta ejecutando
entonces al hacer  if __name__ == '__main__' le estamos preguntando a python si esta ejecutando actualmente
este modulo o es otro importado.
Esto es util por ejemplo si queremos que los metodos de un modulo solo se ejecuten solamente cuando ese
modulo se esta ejecutando, es decir si otro modulo importa a este, que este que lo importa
no pueda ejecutar sus metodos
'''

print("File __name__ : {}".format(__name__)) #imprimira name

def saludo():
    print("Hola")
if __name__ == "__main__":
     saludo()
else:
    print("No se puede ejecutar este metodo fuera del modulo original")
