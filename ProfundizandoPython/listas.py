#Las listas son mutables


nombres1=["juan","luis","karla"]
nombres2='Laura Maria Gonzalo Ernesto'.split()
#sumar listas}
print(f'sumas listas {nombres1+nombres2}')
#extender una lista con otra lista

nombres1.extend(nombres2)
print(f'extender lista nombres1 con nombres 2 {nombres1}')

#lista de numero
numeros=[1,2,13,2,34,456,234,2]
#obtener indice del primer elemnto encontrado en una lista
#help(list.index)

print(f'Indice del numero 2:---- {numeros.index(2)}')

#invertir orden de los elemtos de una lista

numeros.reverse()
print(f'lista invertida {numeros}')

#ordenar los elemntos de una lista
numeros.sort()
print(f'lista ordenada ascendente {numeros}')
#odrnar de manera descendet
numeros.sort(reverse=True)
print(f'lista ordenada desendenter {numeros}')
#obtener valor minimo y maximo de una lista
print(f'minimo:{min(numeros)} maximo:{max(numeros)}')
#copiar elementos de una lista
numeros2=numeros.copy()
print(numeros2)
#preguntas de mismo indice
print(numeros is numeros2)
#preguntar mismo contenido
print(numeros==numeros2)
numeros2=list(numeros)
#preguntas de mismo indice
print(numeros is numeros2)
#preguntar mismo contenido
print(numeros==numeros2)
#slincing
numeros2=numeros[:]
print(numeros is numeros2)
#preguntar mismo contenido
print(numeros==numeros2)
#multiplicacion de listas
multiplicacion=5*[[2,5]]
print(multiplicacion)
print(multiplicacion[0]is multiplicacion[1])
print(multiplicacion[0] == multiplicacion[1])
multiplicacion[2].append(10)
print(multiplicacion)

#matrices en python
matriz=[[10,20],[30,40,50],[60,70,80,90]]
print(matriz)
print(f'Renglon 0 columna 0 :{matriz[0][0]}')
print(f'Renglon 2 columna 3 :{matriz[2][3]}')
matriz[2][0]=65
print(matriz)

#ordenamiento
lista_listas=[[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
print(lista_listas)
#ordenamiento carqacteres
#started built-in
#help(sorted)

nombres1=['juan carlos','karla','pedro','esperanza']
nombres1=sorted(nombres1)
print(nombres1)
nombres1=sorted(nombres1,reverse=True)
print(nombres1)
#ordfenar por la cantidad de caracteres
nombres1=sorted(nombres1,key=len)
print(nombres1)
#build-in reversed
nombres1=reversed(nombres1)
print(list(nombres1))


