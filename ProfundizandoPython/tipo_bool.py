#bool contiene valores de True y False
#Tipo numerico (int y float) False para el valor de cero y True para los demasvalores

valor=0
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')
valor=5
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')

#tipo string, false para '' , true demas valores

valor=''
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')
valor='asdsad'
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')


#tipo colecciones false para colecciones vacias y true para los demas valores

valor=[]
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')
valor= [1,2,3]
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')

#tupla

valor=()
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')
valor= (2,3)
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')

#diccionario

valor={}
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')
valor= {'nobre':'juan','apellido':'lopez'}
resultado=bool(valor)
print(f'valor: {valor}, resultado: {resultado}')


if '':
    print('regreso verdadero')
else:
    print('regreso falso')


if bool('asdasd'):
    print('regreso verdadero')
else:
    print('regreso falso')