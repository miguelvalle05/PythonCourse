#decoradores
#es una funcion que recibe a su vez una funcion y regresa otra
#la utilizamos para xtender funcionalidad
# 1.- funcion decoradora a
# 2.- funcion decorar b
# 3.- funcion decorada c


def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args,**kwargs):
        print('antes de ejecutar la fucnion')
        resultado =funcion_a_decorar_b(*args,**kwargs)
        print('despuyes de ejecutar la funcion')
        return resultado
    return funcion_decorada_c





# @funcion_decorador_a
# def mostrar_mensaje():
#     print('hola desde funcion mostrar mensaje')
#
# mostrar_mensaje()
@funcion_decorador_a
def sumar(a,b):
    return a+b

resultado=sumar(3,10)
print(f'el resultado de la suma es: {resultado}')