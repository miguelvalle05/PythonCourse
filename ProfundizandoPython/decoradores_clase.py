#decoradores de clase
#permiten tranformar de manera programatica nuestra clase, es similar a decoradores de funciones
def decorador_repr(cls):
 print("se ejecuta decorador")

 print(f'recibimos el objeto de la clase:{cls.__name__}')
 
 #revisamos los atributos de la clase con el metodo vars

 atributos=vars(cls)
 #iteramos cada uno de los atributos que viene en un diccionario

 for nombre,atributo in atributos.items():
    print(nombre,atributo)

 #revisamos si se a sobreescrito el metodo init
 if '__init__' not in atributos:
    raise TypeError(f'{cls.__name__} no ha sobreescrito el metodo __init__')

 
 return cls

@decorador_repr
class Persona:
    def __init__(self,nombre,apellido):
        print('se ejecuta el inizializador')
        self._nombre=nombre
        self._apellido=apellido


    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido


persona1=Persona("junaito","lopez")


















