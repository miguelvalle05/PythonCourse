# las funciones en python son ciudadanos de primera clase
#first class  citizens

#definimos la funcion

def sumar(a,b):
    return a+b

#primer uso asignar una funcion a una variable(no se usan paratensuis

mi_funcion=sumar

#verificar tipo de la variable

print(type(mi_funcion))

#llamamos la funciona traves de la variablñe

resultado=mi_funcion(4,3)

print(resultado)



#segundo uso: funcion como argumento



def operacion(a,b,sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a,b)}')


operacion(10,4,sumar)

#3 podemos retornar una funcion

def retornar_funcion():

    #retornamos unafuncion
    return sumar


mi_funcion_retornada= retornar_funcion()

print(f'la funcion retornada {mi_funcion_retornada(12,23)}')


