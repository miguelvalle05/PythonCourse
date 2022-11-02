# with open('prueba.txt','r',encoding='utf8') as archivo:
#     print(archivo.read())
from manejoarchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())