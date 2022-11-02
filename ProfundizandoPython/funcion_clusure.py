#un clusure es una funcion que define a otra y ademas la puede regresar
#la funcion anidada puede acceder a las variables de la funcion porincipal o externa



#funcion principal

# def oprecion(a,b):
#     #definimos una funcion interna o anidad
#     def sumar():
#         return a+b
#
#     #retornar la funcion
#
#     return sumar

#funcion lambda

def operacion(a,b):
    # funcion lambda
    return lambda: a+b



mi_funcion_clusure=operacion(3,7)
print(f'Mi funcion clusure: {mi_funcion_clusure()}')

#ejecutar una funcion
print(f'Mi funcion directamente: {operacion(3,4)()}')