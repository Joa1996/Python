# Es una manera de aplicar la reutilizacion de Codigo (Codigo limpio) en
# Python, la idea es que una funcion recibe como argumento una funcion para dar como
# salida otra funcion  f(a)->b
def  funcion_decoradora(funcion_como_parametro):
      #la funcion decorador recibe como parametro la "funcion a decorar"
    def funcion_interior(*args):#Se necesita esta funcion para dar como salida la funcion
        print("Vamos a realizar el siguiente calculo")
        funcion_como_parametro(*args) #En caso de que nuestros metodos trabajen con parametros sera necesario pasarselos aqui
#En este caso funcion_interior sera la encargada de ejecutar el metodo a decorar, teniendo la
#posibildiad de agregar nuevas funcionalidades como en este ejemplo imprimir algo antes
        print("El resultado fue el anterior")

    return funcion_interior


#Sin parametros
# @funcion_decoradora
# def suma ():
#     print(5+10)
# @funcion_decoradora
# def resta ():
#     print(5-10)
#Con parametros

@funcion_decoradora
def suma (n1,n2):
    print(n1+n2)
@funcion_decoradora
def resta (n1,n2):
    print(n1-n2)

suma(3,2)
resta(5,6)