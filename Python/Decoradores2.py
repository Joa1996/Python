import time
'''
Un ejemplo de uso podria ser conectarse a una BD antes de ejecutar el metodo y cerrar la conexion despues,
o por ejemplo calcular el tiempo de ejecucion de cada metodo
'''
def  funcion_decoradora(funcionadecorar):
    #la funcion decorador recibe como parametro la "funcion a decorar"

    def funcion_interior(*args): #Se necesita esta funcion para dar como salida la funcion
        start=time.time()
        funcionadecorar(*args) #En caso de que nuestros metodos trabajen con parametros sera necesario pasarselos aqui
        print('Tiempo Total:',time.time()-start)
    return funcion_interior



@funcion_decoradora
def suma (n1,n2):
    print(n1+n2)
@funcion_decoradora
def resta (n1,n2):
    print(n1-n2)

suma(3,2)
resta(5,6)