#profundizando en tuplas

#declarar variables
a,b='hola','adios'
print(a,b)
#swap(intercambnio)
a,b=b,a
print(a,b)
#regrresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos),max(elementos)

min,max=minmax([1,2,3,4,5])
print(f'minimo:{min},max:{max}')

#regresar la suma de una tupla

resultado=sum((1,2,3,4,5))
print(resultado)

def sumar(*args):
    return sum(args)

resultado=sumar(1,2,3,2,1,23)
print(resultado)