#print(dir(__builtins__))
#help(zip)

numeros=[1,2,3]
letras=['a','b','c','d']
identificadores=321,322,323,324,325
conjunto={6,4,0,9,8,15,10}
mezcla=zip(numeros,letras,identificadores,conjunto)
print(list(mezcla))
print(tuple(zip(numeros,letras)))

#iterar en partalelo
for numero,letra,id,aleatorio in zip(numeros,letras,identificadores,conjunto):
    print(f'Numero:{numero},Letra{letra},Identificador{id},Conjunto{aleatorio}')

#nueva lista
nueva_lista=[]
for numero,letra,id,aleatorio in zip(numeros,letras,identificadores,conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')

print(nueva_lista)



#unzip
mezcla=[(1,'a'),(2,'b'),(3,'c')]
numeros, letras=zip(*mezcla)
print(numeros)
print(letras)

#ordenamiento usando zip

letras=['c','d','a','e','b']
numeros=[3,0,2,5,1]
mezcla=zip(letras,numeros)
print(tuple(mezcla))
#ordenar por letra
print(sorted(zip(letras,numeros)))
#ordenar por letra
print(sorted(zip(numeros,letras)))
#crear un diccionario con zip y dos variables

llaves=['Nombre','Apellido','Edad']
valores=['Juan','Peres',18]
diccionario=dict(zip(llaves,valores))
print(diccionario)
#actualizar elemento de nuestro diccionario
llave=['Edad']
nueva_edad=[28]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)