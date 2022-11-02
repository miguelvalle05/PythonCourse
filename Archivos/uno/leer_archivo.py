archivo=open('prueba.txt','r',encoding='utf8')
#print(archivo.read())

#leer algunos carcateres

#print(archivo.read(5))
#print(archivo.read(4))


#leer lineas completas

#print(archivo.readline())
#print(archivo.readline())

#iterar achivo


# for linea in archivo:
#     print(linea)


# print(archivo.readlines())

# print(archivo.readlines()[2])


#abrimos nuervo arcihvo

archivo2=open('copia.txt','a',encoding='utf8')
archivo2.write(archivo.read())

archivo2.close()
archivo.close()

print('se copiaron archivos')