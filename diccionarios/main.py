diccionario={
    'IDE': 'integret development Enviroment',
    'OPP': 'Object Oriented Programming',
    'DBMS': 'database management system'}

len(diccionario)
print(diccionario['IDE'])
print(diccionario.get('OPP'))


for termino, valor in diccionario.items():
    print(termino, valor)


for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#existencia de algun elemento

print('IDE' in diccionario)

#agregar
diccionario['pk']= 'primary key'
print(diccionario)

#remover
diccionario.pop('IDE')
print(diccionario)