nombres = ['juan','ricado','karla','maria']
print(nombres)
print(nombres[-1])
print(nombres[:3])
print(nombres[:])
#cambiar dato de lista
nombres[3]='juanitooooo'
print(nombres)
#iterar lista
for nombre in nombres:
    print(nombre)
#longitud de la lista
print(len(nombres))
#agregar elemento
nombres.append('lucero')
print(nombres)
#insertar elemnto en posicion especifico

nombres.insert(1,'alex')
print(nombres)

#remover un elemento
nombres.remove('alex')
print(nombres)

#elminar ultimo valor de la lista
nombres.pop()
print(nombres)

#eliminar indice especifico
del nombres[0]
print(nombres)
#limpiar lista
nombres.clear()
print(nombres)
#borrar lista por completo
del nombres


for i in range(10):
    if i%3==0:
     print(i)