# #funciones lambda: funciones anonimas no tiene un nombre asigando y tambien son pequeñas, es solo
# una line  de codigo

#
# def sumar(a,b):
#     return a+b


#con una funcion lambda la funcion es anonima y una solo linea de codigo
# no se necesita return ni parentesis para los parametros

mi_funcion_lambda=lambda a,b: a+b


result= mi_funcion_lambda(3,4)
print(f'funcion lambda {result}')

#funcion lambda que no recibi argumentos(debemos regresa una expresion valida)

mi_funcion_lambda = lambda: 'Funcion sin argumentos'
print(f'llamar funcion lambda sin parametros {mi_funcion_lambda()}')

#funcion lambda cion parametros por default
mi_funcion_lambda= lambda a=2, b=3: a+b
result=mi_funcion_lambda()
print(f'funcion con valores por default: {result}')

#funcion lambda con argumentos varibles *args y **kwargs
mi_funcion_lambda=lambda *args,**kwargs: len(args)+ len(kwargs)
print(f' funcion con parametros variables {mi_funcion_lambda(1,2,3,4, a=2, b=3)}')


#dunciones vairables con argumentos, artgumentos variables y argumentos por default
mi_funcion_lambda = lambda a,b,c,d=3,*args, **kwargs: a+b+c+d+len(args)+len(kwargs)

print(f'funcion lambda aplicando todo: {mi_funcion_lambda(2,3,3, 4,5,4,5,e=3,f=3)}')