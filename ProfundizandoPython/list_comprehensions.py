numeros=range(10)
lista_pares=[]


#creamos una nueva lista con los valores pares

for numero in numeros:
    if numero%2==0:
        lista_pares.append(numero*numero)


print(f'lista de pares: {lista_pares}')

#haacemos los mismo pero con los comprenhensions
#expresion for y coleccion luego un if

lista_pares=[]

lista_pares=[numero*numero for numero in numeros if numero%2==0]
print(lista_pares)

#ejemplo similar con doscondiciones
#solo se agrega el valor a la lista cuando el valor cumple ambas condiocioens
#numero divisible entre 2 y tambien entre 6
pares=[numero for numero in range(50) if numero%2==0 if numero%6==0]
print(pares)


#ejemplo agregando if else
lista_pares=[]
lista_impares=[]

for numero in range(10):
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)


print(f'lista de pares{lista_pares} lsiata de impares{lista_impares}')


#mismo ejempli usando list comprehensions
lista_pares=[]
lista_impares=[]
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range(20)]
print(f'lista impares {lista_impares}')
print(f'lista parees:{lista_pares}')

#lista de listas

listas_listas=[[1,2,3],[4,5,6],[7,8,9,10]]
# convertimos la liustas de litas en una sola lista

lista_simple=[valor for sublista in listas_listas for valor in sublista]
print(lista_simple)

lista_pares=[]

#lista de nuemros pares a partir de la lista de liastas

for sublista in listas_listas:
    for valor in sublista:
        if valor%2==0:
            lista_pares.append(valor)

print(lista_pares)


lista_pares=[]
#con list comprehensions
lista_simple=[valor for sublista in listas_listas for valor in sublista if valor%2==0]
print(lista_simple)
