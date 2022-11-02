frutas= ('naranja', 'manzana', 'platano')
print(frutas)
#largo de tupla
print(len(frutas))

print(frutas[0])

for fruta in frutas:
    print(fruta, end=' ')


frutalista= list(frutas)

frutalista[2]='limon'
print(frutalista)

frutas=tuple(frutalista)
print(frutas)

numeros=(13,1,8, 3, 2, 5, 8)
lista=[]

for i in numeros:
    if i<=5:
     lista.append(i)

print(lista)

planetas={'marte','jupiter','venus'}
planetas.add('Tierra')
print(planetas)
print('marte' in planetas)
planetas.remove('Tierra')
planetas.discard('eee')