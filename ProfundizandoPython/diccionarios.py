from pprint import pprint as pp

#profundizando en diccionarios

#Los diccionarios guardan un orden a diferencia de un set

diccionario={'nombre':'juan','aplleido':'perez','edad':28}
print(diccionario)

#los diccionarios son mutables pero las llaves son inmutables

diccionario={(1,2):'valor1'}
print(diccionario)

#se agrega una llave con su valor si no se encuentra dentro del diccionario

diccionario['Departamento']='sistemas'
print(diccionario)

#los diccionarios no tiene valores duplicados en las llaves

diccionario['Departamento']='Almacen'
print(diccionario)

#Recuperar elementos de un diccionario
print(diccionario['Departamento'])
#Si no encuentra la llave lanza una exepcion
print(diccionario['Departamento'])
#metodo get recupera una llave y si no existe no lanza una exepcion
#ademas puede regresarse un valor de que no exista la variable
print(diccionario.get('Departameto','Nose encontro la lave'))

#setdefault, se modifica el diccionario en caso de que nose encuentre la llave y se agrega un valor por default}
print(diccionario.setdefault('Deartamento','valor por defauñt'))
print(diccionario)

#pprint

pp(diccionario,sort_dicts=False)