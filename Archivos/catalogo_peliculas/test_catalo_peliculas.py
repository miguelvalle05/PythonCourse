from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion=None


while opcion!=4:

       try:
            print('opciones: ')
            print('1.- Agregar peliculas')
            print('2.- Listar peliculas')
            print('3.- Eliminar peliculas')
            print('4.- Salir')
            opcion=int(input('Escribe una opcion '))

            if opcion==1:
                nombre_pelicula=input('proporciona el nombre de la pelicula')
                pelicula=Pelicula(nombre_pelicula)
                cp.agregar_pelicula(pelicula)

            elif opcion==2:
                cp.listar_peliculas()
            elif opcion==3:
                cp.elminar_peliculas()




       except Exception as e:
           print(f'Ocurrio un error {e}')
           opcion=None

else:
    print('salimos del programa')




