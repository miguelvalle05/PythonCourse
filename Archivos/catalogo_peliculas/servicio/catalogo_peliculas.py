import os

class  CatalogoPeliculas:


    rutaarchivo='peliculas.txt'

    @classmethod

    def agregar_pelicula(cls,pelicula):
        with open(cls.rutaarchivo,'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod

    def listar_peliculas(cls):
        with open(cls.rutaarchivo, 'r', encoding='utf8') as archivo:
            print('Catalogo de peliculas'.center(50,'-'))
            print(archivo.read())

    @classmethod

    def elminar_peliculas(cls):
        os.remove(cls.rutaarchivo)
        print(f'archivo elminado {cls.rutaarchivo}')


        
